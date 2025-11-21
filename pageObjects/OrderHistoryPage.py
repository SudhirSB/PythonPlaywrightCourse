from .OrderDetailsPage import OrdersDetailsPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def select_order(self,order_id):
        order_row = self.page.locator("table tbody tr").filter(has_text=order_id)
        order_row.locator("td").get_by_role("button", name="View").click()
        order_details_page = OrdersDetailsPage(self.page)
        return order_details_page