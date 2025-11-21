from playwright.sync_api import expect


class OrdersDetailsPage:
    def __init__(self,page):
        self.page = page

    def validate_order_message(self,expected_message):
        expect(self.page.locator("div.email-preheader")).to_have_text(expected_message)