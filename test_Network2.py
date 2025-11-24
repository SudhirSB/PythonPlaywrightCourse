import time

import pytest
from playwright.sync_api import Page, expect, Playwright
from utils.APIBase import APIUtils

fake_response_payload = {"data":[],"message":"No Orders"}

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_with_network_interception(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("sudhirsu17@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("13579@RahulShettyAcademy")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    page.get_by_role("button",name="View").first.click()
    expect(page.locator("p.blink_me")).to_have_text("You are not authorize to view this order")

@pytest.mark.smoke
def test_session_storage(playwright: Playwright):
    # Get token with API call
    api_utils = APIUtils()
    token = api_utils.generate_token(playwright)

    # Launch browser and set session storage
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem("token", "{token}");""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="Orders").click()
    expect(page.locator('h1.ng-star-inserted')).to_have_text("Your Orders")
    expect(page.get_by_text("Your Orders")).to_be_visible()