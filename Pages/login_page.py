from Pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    def open(self):
        self.goto(self.URL)

    def login(self, username: str, password: str):
        self.fill("input[data-test='username']", username)
        self.fill("input[data-test='password']", password)
        self.click("input[data-test='login-button']")