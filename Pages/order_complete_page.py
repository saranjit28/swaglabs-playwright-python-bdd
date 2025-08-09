from Pages.base_page import BasePage

class OrderCompletePage(BasePage):
    def get_confirmation_message(self) -> str:
        return self.get_text(".complete-header")
