from src.core.base.base_page import BasePage
from src.core.pagelocators.meeting_page_locators import MeetingPageLocators
from src.core.utils.logger import Logger

class MeetingPage(BasePage, MeetingPageLocators):
    logger = Logger(__name__)

    # Constructor
    def __init__(self, driver):
        super(MeetingPage, self).__init__(driver)

    def jump15Forward(self):
        self.logger.info(f'Invoking `jump15Forward`...')
        try:
            self.wait_click(self.FORWARDS_BTN)
        except Exception as e:
            self.logger.error(err)
            raise e

    def jump15Backwards(self):
        self.logger.info(f'Invoking `jump15Backwards`...')
        try:
            self.wait_click(self.BACKWARDS_BTN)
        except Exception as e:
            self.logger.error(err)
            raise e

    def click_play(self):
        self.logger.info(f'Invoking `click_play`...')
        try:
            self.wait_click(self.PLAY_BTN)
        except Exception as e:
            self.logger.error(err)
            raise e

    def click_pause(self):
        self.logger.info(f'Invoking `click_pause`...')
        try:
            self.wait_click(self.PAUSE_BTN)
        except Exception as e:
            self.logger.error(err)
            raise e

    def get_durations(self):
        self.logger.info(f'Invoking `get_durations`...')
        try:
            return self.get_text(self.DURATION_TEXT)
        except Exception as e:
            self.logger.error(err)
            raise e

    def wait_before_action(self, sec: int):
        self.logger.info(f'Invoking `wait_before_action` for {sec} seconds')
        try:
            self.wait(sec)
        except Exception as e:
            self.logger.error(err)
            raise e
