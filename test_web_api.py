import json
import pytest

from playwright.sync_api import Playwright
from pageObjects.LoginPage import LoginPage
from utils.APIBaseFramework import APIUtils

# pytest -n 3 --browser_name webkit --html=report.html --tracing on -m smoke

#Get Test Data from the json file
with open("data/credentials.json") as f:
    test_data = json.load(f)
    credentials_list = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize('credentials',credentials_list)
def test_place_order_and_verify(playwright:Playwright, browser_instance, credentials):
    #place order via API
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, credentials)

    #Login to UI
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    dashboard_page = login_page.login(credentials["username"], credentials["password"])

    #Validate order in UI
    order_history_page = dashboard_page.navigate_to_orders()
    order_details_page = order_history_page.select_order(order_id)
    order_details_page.validate_order_message("Thank you for Shopping With Us")