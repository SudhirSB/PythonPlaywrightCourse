from playwright.sync_api import Page, expect, Playwright


def test_invalid_login(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningasdas")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_invalid_login_using_firefox(playwright:Playwright):
    firefox_browser = playwright.firefox.launch()
    context = firefox_browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningasdas")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms").check()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
