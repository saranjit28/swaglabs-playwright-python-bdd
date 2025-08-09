from Pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    finish_button = "#finish"

    def finish_checkout(self):
        self.click(self.finish_button)
