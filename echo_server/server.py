"""Echo-сервер: возвращает клиенту метод, адрес и заголовки его запроса."""

import socket
from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

HOST = "127.0.0.1"
PORT = 5000


def parse_request(data: bytes) -> tuple[str, str, list[str]]:
    """Разбирает сырой HTTP-запрос на метод, путь и список строк-заголовков."""
    lines = data.decode("utf-8").split("\r\n")
    method, path, _version = lines[0].split(" ")

    headers = []
    for line in lines[1:]:
        # Пустая строка отделяет заголовки от тела запроса
        if line == "":
            break
        headers.append(line)

    return method, path, headers


def get_status(path: str) -> HTTPStatus:
    """Возвращает статус из GET-параметра status.

    Если параметр не передан или невалиден, возвращает 200 OK.
    """
    params = parse_qs(urlparse(path).query)
    values = params.get("status")
    if not values:
        return HTTPStatus.OK

    try:
        return HTTPStatus(int(values[0]))
    except ValueError:
        # Не число или несуществующий код статуса
        return HTTPStatus.OK


def build_response(
    method: str, source: tuple, status: HTTPStatus, headers: list[str]
) -> bytes:
    """Собирает HTTP-ответ, в теле которого перечислены данные запроса."""
    body_lines = [
        f"Request Method: {method}",
        f"Request Source: {source}",
        f"Response Status: {status.value} {status.phrase}",
        *headers,
    ]
    body = "\r\n".join(body_lines).encode("utf-8")

    response_head = (
        f"HTTP/1.1 {status.value} {status.phrase}\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    return response_head.encode("utf-8") + body


def run_server(host: str = HOST, port: int = PORT) -> None:
    """Запускает сервер и обрабатывает клиентов по одному, не завершаясь."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущен на http://{host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                data = conn.recv(1024)
                # Браузеры иногда закрывают соединение, ничего не отправив
                if not data:
                    continue

                try:
                    method, path, headers = parse_request(data)
                except ValueError:
                    print(f"{addr} некорректный запрос: {data!r}")
                    continue

                status = get_status(path)
                conn.sendall(build_response(method, addr, status, headers))
                print(f"{addr} {method} {path} -> {status.value}")


if __name__ == "__main__":
    run_server()
