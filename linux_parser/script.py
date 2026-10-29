"""Парсер вывода команды ps aux: отчёт о состоянии системы."""
import subprocess
from datetime import datetime
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent.parent / "script_reports"


def get_processes() -> str:
    """Запускает ps aux и возвращает её вывод строкой."""
    result = subprocess.run(
        ["ps", "aux"],
        capture_output=True,
        text=True,
    )
    return result.stdout


def parse_processes(output: str) -> list[dict]:
    """Разбирает вывод ps aux в список словарей."""
    processes = []
    lines = output.strip().split("\n")
    for line in lines[1:]:
        columns = line.split(maxsplit=10)
        processes.append({
            "user": columns[0],
            "cpu": float(columns[2]),
            "mem": float(columns[3]),
            "command": columns[10],
        })
    return processes


def collect_stats(processes: list[dict]) -> dict:
    """Считает статистику по списку процессов."""
    users_count = {}
    for process in processes:
        user = process["user"]
        users_count[user] = users_count.get(user, 0) + 1

    total_mem = sum(process["mem"] for process in processes)
    total_cpu = sum(process["cpu"] for process in processes)

    top_mem = max(processes, key=lambda process: process["mem"])
    top_cpu = max(processes, key=lambda process: process["cpu"])

    return {
        "users": users_count,
        "total": len(processes),
        "mem": round(total_mem, 1),
        "cpu": round(total_cpu, 1),
        "top_mem": top_mem["command"][:20],
        "top_cpu": top_cpu["command"][:20],
    }


def build_report(stats: dict) -> str:
    """Формирует текст отчёта по статистике."""
    users = ", ".join(f"'{user}'" for user in stats["users"])
    users_lines = "\n".join(f"{user}: {count}" for user, count in stats["users"].items())

    return (
        "Отчёт о состоянии системы:\n"
        f"Пользователи системы: {users}\n"
        f"Процессов запущено: {stats['total']}\n"
        "\n"
        "Пользовательских процессов:\n"
        f"{users_lines}\n"
        "\n"
        f"Всего памяти используется: {stats['mem']}%\n"
        f"Всего CPU используется: {stats['cpu']}%\n"
        f"Больше всего памяти использует: {stats['top_mem']}\n"
        f"Больше всего CPU использует: {stats['top_cpu']}\n"
    )


def save_report(report: str) -> Path:
    """Сохраняет отчёт в txt-файл с текущей датой и временем в названии."""
    REPORTS_DIR.mkdir(exist_ok=True)
    file_name = datetime.now().strftime("%d-%m-%Y-%H-%M") + "-scan.txt"
    file_path = REPORTS_DIR / file_name
    file_path.write_text(report, encoding="utf-8")
    return file_path


def main() -> None:
    output = get_processes()
    processes = parse_processes(output)
    stats = collect_stats(processes)
    report = build_report(stats)
    print(report)
    file_path = save_report(report)
    print(f"Отчёт сохранён в файл: {file_path}")


if __name__ == "__main__":
    main()