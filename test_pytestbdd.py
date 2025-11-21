import pytest
from playwright.sync_api import Playwright
from pytest_bdd import given, when, then, parsers, scenarios
from pytest_bdd.gherkin_parser import Scenario

from pageObjects.LoginPage import LoginPage
from utils.APIBaseFramework import APIUtils


scenarios('features/OrderTransactions.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("Order is placed with {username} and {password}"))
def place_order(playwright:Playwright, username, password, shared_data):
    print(f"Placing order with {username} and {password}")

    credentials = {"username": username,"password": password}
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, credentials)
    shared_data['order_id'] = order_id
    shared_data['credentials'] = credentials

@given("the user is on the landing page")
def navigate_to_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    shared_data['login_page'] = login_page
    print("Navigated to landing page")

@when(parsers.parse("the user logs in to the application with {username} and {password}"))
def login_to_application(username, password, shared_data):
    credentials = shared_data['credentials']
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(credentials["username"], credentials["password"])
    shared_data['dashboard_page'] = dashboard_page

@when("the user navigated to the orders page")
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_history_page = dashboard_page.navigate_to_orders()
    shared_data['order_history_page'] = order_history_page

@when("selects the order id")
def select_order_id(shared_data):
    order_history_page = shared_data['order_history_page']
    order_id = shared_data['order_id']
    order_details_page = order_history_page.select_order(order_id)
    shared_data['order_details_page'] = order_details_page

@then("the order message is successfully displayed")
def validate_order_message(shared_data):
    order_details_page = shared_data['order_details_page']
    order_details_page.validate_order_message("Thank you for Shopping With Us")