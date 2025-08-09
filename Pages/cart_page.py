from Pages.base_page import BasePage

class CartPage(BasePage):
    checkout_button = "#checkout"

    def proceed_to_checkout(self):
        self.click(self.checkout_button)
