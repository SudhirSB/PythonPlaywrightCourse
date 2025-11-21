from .OrderHistoryPage import OrderHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def navigate_to_orders(self):
        self.page.get_by_role("button", name="Orders").click()
        order_history_page = OrderHistoryPage(self.page)
        return order_history_page