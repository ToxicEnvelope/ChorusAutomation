from src.core.base.base_page import BasePage
from src.core.pagelocators.login_page_locators import LoginPageLocators
from src.core.utils.logger import Logger


class LoginPage(BasePage, LoginPageLocators):
    logger = Logger(__name__)

    # Constructor
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    # Make login method
    def makeLogin(self, credentianls: tuple):
        self.logger.info(f'Invoking `makeLogin` using -> {credentianls}')
        try:
            self.wait_clear_send_keys(self.USERNAME_FIELD, credentianls[0])
            self.wait_click(self.LOGIN_BTN)
            self.wait_clear_send_keys(self.PASSWORD_FIELD, credentianls[1])
            self.wait_click(self.CONTINUE_BTN)
            self.wait(5)
        except Exception as e:
            self.logger.error(err)
            raise e