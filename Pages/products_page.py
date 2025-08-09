from Pages.base_page import BasePage

class ProductsPage(BasePage):
    def add_first_product_to_cart(self):
        self.click("button[data-test='add-to-cart-sauce-labs-backpack']")

    def go_to_cart(self):
        self.click(".shopping_cart_link")