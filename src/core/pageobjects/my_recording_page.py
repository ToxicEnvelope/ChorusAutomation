from src.core.base.base_page import BasePage
from src.core.utils.logger import Logger


class MyRecordingsPage(BasePage):
    logger = Logger(__name__)

    # Constructor
    def __init__(self, driver):
        self.URI = "/my-recordings"
        super(LoginPage, self).__init__(driver, self.URI)
