from src.core.base.base_page import BasePage
from src.core.utils.logger import Logger
from src.core.pagelocators.recordings_page_locators import RecordingsPageLocators

class RecordingsPage(BasePage, RecordingsPageLocators):
    logger = Logger(__name__)

    # Constructor
    def __init__(self, driver):
        self.URI = "/recordings?"
        super(LoginPage, self).__init__(driver, self.URI)

    def clear_filters(self):
        self.logger.info(f'Invoking `clear_filters`...')
        try:
            self.wait_click(self.CLEAR_FILTERS_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err



