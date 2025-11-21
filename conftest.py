import pytest
from playwright.sync_api import Playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser selection"
    )

@pytest.fixture(scope="session")
def credentials(request):
    return request.param

@pytest.fixture
def browser_instance(playwright:Playwright, request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    browser_context = browser.new_context()
    page = browser_context.new_page()
    yield page
    browser_context.close()
    browser.close()