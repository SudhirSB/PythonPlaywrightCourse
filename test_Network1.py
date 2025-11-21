from playwright.sync_api import Page, expect

fake_response_payload = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json=fake_response_payload
    )

def test_with_network_interception(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("sudhirsu17@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("13579@RahulShettyAcademy")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="Orders").click()
    order_text = page.locator(".mt-4")
    expect(page.locator(".mt-4")).to_contain_text("No Orders")