"""Скрипт анализа access.log файлов."""

import argparse
import json
import os
import re
from collections import Counter


LOG_PATTERN = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) \S+ \S+ (\[[^\]]+\]) '
    r'"([A-Z]+) (\S+) [^"]*" \S+ \S+ '
    r'"((?:[^"\\]|\\.)*)" "(?:[^"\\]|\\.)*" (\d+)$'
)


def parse_line(line):
    """Разбирает строку лога в словарь или возвращает None."""
    match = LOG_PATTERN.match(line)
    if match is None:
        return None
    return {
        "ip": match.group(1),
        "date": match.group(2),
        "method": match.group(3),
        "url": match.group(5),
        "duration": int(match.group(6)),
    }


def analyze_file(path):
    """Собирает статистику по лог-файлу за один проход."""
    total_requests = 0
    total_stat = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "DELETE": 0,
        "OPTIONS": 0,
        "HEAD": 0,
    }
    ip_counter = Counter()
    top_longest = []

    with open(path, encoding="utf-8", errors="ignore") as file:
        for line in file:
            total_requests += 1

            parsed = parse_line(line)
            if parsed is None:
                continue

            ip_counter[parsed["ip"]] += 1
            top_longest.append(parsed)
            top_longest.sort(
                key=lambda request: request["duration"], reverse=True
            )
            top_longest = top_longest[:3]

            method = parsed["method"]
            if method in total_stat:
                total_stat[method] += 1

    return {
        "top_ips": dict(ip_counter.most_common(3)),
        "top_longest": top_longest,
        "total_stat": total_stat,
        "total_requests": total_requests,
    }


def save_to_json(stat, log_file, output_dir="results"):
    """Сохраняет статистику в json-файл и возвращает путь к нему."""
    os.makedirs(output_dir, exist_ok=True)
    name = os.path.splitext(os.path.basename(log_file))[0]
    json_path = os.path.join(output_dir, f"{name}.json")
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(stat, file, indent=4, ensure_ascii=False)
    return json_path


def get_log_files(path):
    """Возвращает список лог-файлов по пути к файлу или директории."""
    if os.path.isfile(path):
        return [path]

    if os.path.isdir(path):
        log_files = []
        for name in sorted(os.listdir(path)):
            full_path = os.path.join(path, name)
            if os.path.isfile(full_path) and name.endswith(".log"):
                log_files.append(full_path)
        return log_files

    raise SystemExit(f"Путь не найден: {path}")


def parse_args():
    """Разбирает аргументы командной строки."""
    parser = argparse.ArgumentParser(description="Анализ access.log файлов")
    parser.add_argument(
        "path", help="путь к лог-файлу или директории с логами"
    )
    return parser.parse_args()


def main():
    """Точка входа: анализирует логи и выводит статистику."""
    args = parse_args()
    for log_file in get_log_files(args.path):
        stat = analyze_file(log_file)
        json_path = save_to_json(stat, log_file)
        print(f"Статистика для файла: {log_file}")
        print(json.dumps(stat, indent=4, ensure_ascii=False))
        print(f"Сохранено: {json_path}\n")


if __name__ == "__main__":
    main()
