from playwright.sync_api import Page, expect


def test_UIValidationsDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_label("terms").check()
    page.get_by_role("button", name="Sign In").click()

    i_phone_product = page.locator("app-card").filter(has_text="iphone X")
    i_phone_product.get_by_role("button").click()

    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()

    page.get_by_text("Checkout").click()

    expect(page.locator("div.media")).to_have_count(2)

def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page_info:
        page.locator(".blinkingText").click()
        child_page = new_page_info.value
        text_content = child_page.locator(".red").text_content()
        print(text_content)
        split_text = text_content.split(" ")
        email = split_text[4]
        assert email == "mentor@rahulshettyacademy.com"