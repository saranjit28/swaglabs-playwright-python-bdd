from pytest_bdd import scenarios, given, when, then
from Pages.login_page import LoginPage

scenarios("../features/login.feature")

@given("I am on the login page")
def open_login_page(page):
    login_page = LoginPage(page)
    login_page.open()

@when("I login with valid credentials")
def login_valid_user(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")

@then("I should be on the products page")
def verify_products_page(page):
    assert "inventory" in page.url
