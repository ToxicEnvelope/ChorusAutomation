from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.core.pagelocators.left_facet_locators import LeftFacetLocators
from src.core.utils.logger import Logger
from time import sleep
import abc


class BasePage(metaclass=abc.ABCMeta):
    logger = Logger(__name__)
    BASE_URL = u"https://www.chorus.ai"
    facet = LeftFacetLocators
    _driver: WebDriver

    # Constructor
    def __init__(self, driver):
        self._driver = driver

    # Click method
    def click(self, element):
        self.logger.info(f'Invoking `click` using -> {element}')
        try:
            if element.is_displayed():
                element.click()
        except Exception as err:
            self.logger.error(err)
            raise err

    # Clear and Send Keys method
    def clear_send_keys(self, element, phrase):
        self.logger.info(f'Invoking `clear_send_keys` using -> {element} : {phrase}')
        try:
            if element.is_displayed():
                element.clear()
                element.send_keys(phrase)
        except Exception as err:
            self.logger.error(err)
            raise err

    # Smart Wait Click
    def wait_click(self, tpl_obj):
        self.logger.info(f'Invoking `wait_click` using -> {tpl_obj}')
        try:
            WebDriverWait(self._driver, 10)\
                .until(EC.visibility_of_element_located(tpl_obj)).click()
        except Exception as err:
            self.logger.error(err)
            raise err

    # Smart Wait Clear and Send Keys
    def wait_clear_send_keys(self, tpl_obj, phrase):
        self.logger.info(f'Invoking `wait_clear_send_keys` using -> {tpl_obj} : {phrase}')
        try:
            elem = WebDriverWait(self._driver, 10) \
                .until(EC.visibility_of_element_located(tpl_obj))
            if elem.is_displayed():
                elem.clear()
                elem.send_keys(phrase)
        except Exception as err:
            self.logger.error(err)
            raise err

    def to_webelement(self, tpl_obj):
        self.logger.info(f'Invoking `to_webelement` using -> {tpl_obj}')
        try:
            return WebDriverWait(self._driver, 10) \
                .until(EC.visibility_of_element_located(tpl_obj))
        except Exception as err:
            self.logger.error(err)
            raise err

    def get_text(self, tpl_obj):
        self.logger.info(f'Invoking `get_text` using -> {tpl_obj}')
        try:
            return WebDriverWait(self._driver, 10) \
                .until(EC.visibility_of_element_located(tpl_obj)).text
        except Exception as err:
            self.logger.error(err)
            raise err

    def nav_from_facet(self, tpl_obj):
        self.logger.info(f'Invoking `nav_from_facet` using -> {tpl_obj}')
        try:
            self.wait_click(tpl_obj)
        except Exception as err:
            self.logger.error(err)
            raise err

    def wait(self, time: int):
        self.logger.info(f'Invoking `wait` for {time} seconds')
        try:
            sleep(time)
        except Exception as err:
            self.logger.error(err)
            raise err

    ## FACET USAGE ##

    def navToSearchPage(self):
        self.logger.info(f'Invoking `navToSearchPage`...')
        try:
            self.nav_from_facet(self.facet.SEARCH_BTN_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err

    def navToMyRecordsPage(self):
        self.logger.info(f'Invoking `navToMyRecordsPage`...')
        try:
            self.nav_from_facet(self.facet.MY_RECORDS_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err

    def navToRecordingPage(self):
        self.logger.info(f'Invoking `navToRecordingPage`...')
        try:
            self.nav_from_facet(self.facet.RECORDINGS_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err

    def navToDealsPage(self):
        self.logger.info(f'Invoking `navToDealsPage`...')
        try:
            self.nav_from_facet(self.facet.DEALS_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err

    def navToCoachingPage(self):
        self.logger.info(f'Invoking `navToCoachingPage`...')
        try:
            self.nav_from_facet(self.facet.COACHING_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err

    def navToAnalysisPage(self):
        self.logger.info(f'Invoking `navToAnalysisPage`...')
        try:
            self.nav_from_facet(self.facet.ANALYSIS_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err

    def navToPlaylistPage(self):
        self.logger.info(f'Invoking `navToPlaylistPage`...')
        try:
            self.nav_from_facet(self.facet.PLAYLIST_BTN)
        except Exception as err:
            self.logger.error(err)
            raise err


