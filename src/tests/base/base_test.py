import unittest
from selenium import webdriver
from src.core.utils import GlobalConfig
from src.core.utils.logger import Logger

class BaseTest(unittest.TestCase):
    logger = Logger(__name__)

    # variables -- driver, URL, etc...
    driver = None
    URL = "https://chorus.ai/meeting/602925?tab=summary&call=415473F6505845088F020C86560C2762"

    # Setup before each TEST
    def setUp(self):
        self.logger.info(f'Invoking `setUp`...')
        try:
            chrome_driver = str.format('{0}/78/chromedriver.exe', GlobalConfig.get_bin_dir())
            self.driver = webdriver.Chrome(chrome_driver)
            self.driver.get(self.URL)
            self.driver.maximize_window()
        except Exception as e:
            self.logger.error(e)
            raise e

    # TearDown after each TEST
    def tearDown(self):
        self.logger.info(f'Invoking `tearDown`...')
        try:
            if self.driver is not None:
                self.driver.quit()
        except Exception as e:
            self.logger.error(e)
            raise e

if __name__ == '__main__':
    unittest.main()
