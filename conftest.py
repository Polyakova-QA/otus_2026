def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption(
        "--browser_version",
        default=None,
        help="версия браузера; если не указана — берётся версия по умолчанию из browsers.json",
    )
    parser.addoption("--base_url", default="http://localhost:8081/")
    parser.addoption(
        "--executor",
        default="local",
        help="local — браузер на этой машине, иначе имя хоста с WebDriver (например, ggr)",
    )
