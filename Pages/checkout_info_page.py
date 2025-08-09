from Pages.base_page import BasePage

class CheckoutInfoPage(BasePage):
    first_name_input = "#first-name"
    last_name_input = "#last-name"
    postal_code_input = "#postal-code"
    continue_button = "#continue"

    def fill_information(self, first_name, last_name, postal_code):
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)
        self.click(self.continue_button)
