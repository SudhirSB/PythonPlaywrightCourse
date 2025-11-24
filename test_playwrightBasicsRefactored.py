from playwright.sync_api import Page, expect, Playwright

# Centralized test configuration
URL = "https://rahulshettyacademy.com/loginpagePractise/"
DEFAULT_USERNAME = "rahulshettyacademy"
DEFAULT_PASSWORD = "learningasdas"
DEFAULT_ROLE = "teach"
EXPECTED_ERROR_TEXT = "Incorrect username/password."


def _perform_invalid_login(page: Page, username: str = DEFAULT_USERNAME, password: str = DEFAULT_PASSWORD, role: str = DEFAULT_ROLE) -> None:
    """Reusable flow for performing an invalid login and asserting the error message.

    Parameters:
    - page: Playwright page object to operate on.
    - username/password/role: optional overrides for the credentials/role.
    """
    page.goto(URL)
    page.get_by_label("Username:").fill(username)
    page.get_by_label("Password:").fill(password)
    page.get_by_role("combobox").select_option(role)
    page.get_by_label("terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text(EXPECTED_ERROR_TEXT)).to_be_visible()


def test_invalid_login(page: Page):
    """Run the invalid login flow using the pytest-playwright `page` fixture."""
    _perform_invalid_login(page)


def test_invalid_login_using_firefox(playwright: Playwright):
    """Run the invalid login flow against an explicit Firefox browser instance.

    This demonstrates running the same flow on a manually launched browser and ensures
    the browser/context are always closed even if assertions fail.
    """
    firefox_browser = playwright.firefox.launch()
    context = firefox_browser.new_context()
    page = context.new_page()
    try:
        _perform_invalid_login(page)
    finally:
        # Always clean up resources to avoid leaking browser processes in CI/local runs
        context.close()
        firefox_browser.close()

