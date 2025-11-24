import time

from playwright.sync_api import Page, expect, Playwright


def test_additionalUIValidations(playwright:Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://www.rahulshettyacademy.com/AutomationPractice/")

    #Hide/Display and placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    page.get_by_role("button", name="Show").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    #AlertBoxes
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()

    #Frame Handling
    page_frame = page.frame_locator("#courses-iframe")
    page_frame.get_by_role("dialog").wait_for()
    expect(page_frame.get_by_role("dialog")).to_contain_text("The IT Recruitment System is Broken.")

    # Mouse Hover
    page.get_by_role("button", name="Mouse Hover").hover()
    page.get_by_role("link", name="Top").click()

    #Table handling
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    price_col_index = -1
    for i in range(page.locator("table.table th").count()):
        if page.locator("table.table th").nth(i).filter(has_text="Price").count()>0:
            price_col_index = i
            break
    print("Price columns index is:", price_col_index)
    assert price_col_index != -1

    rice_row = page.locator("table.table tbody tr").filter(has_text="Rice")
    rice_price = rice_row.locator("td").nth(price_col_index).text_content()
    expect(rice_row.locator("td").nth(price_col_index)).to_have_text("37")
    print("Rice price is:",rice_price)
    assert(int(rice_price)) == 37