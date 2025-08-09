from pytest_bdd import scenarios, given, when, then
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from Pages.order_complete_page import OrderCompletePage

scenarios("../features/order.feature")

@given("I am logged in")
def logged_in(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

@when("I add a product to the cart and checkout")
def checkout_product(page):
    products_page = ProductsPage(page)
    products_page.add_first_product_to_cart()
    products_page.go_to_cart()
    page.click("button[data-test='checkout']")
    page.fill("input[data-test='firstName']", "John")
    page.fill("input[data-test='lastName']", "Doe")
    page.fill("input[data-test='postalCode']", "12345")
    page.click("input[data-test='continue']")
    page.click("button[data-test='finish']")

@then("I should see order confirmation")
def verify_order(page):
    order_page = OrderCompletePage(page)
    confirmation = order_page.get_confirmation_message()
    assert confirmation.lower() == "thank you for your order!"
