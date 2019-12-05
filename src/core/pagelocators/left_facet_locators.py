from selenium.webdriver.common.by import By

class LeftFacetLocators:
    SEARCH_BTN = (By.CSS_SELECTOR, "reports-nav > div > a.search > div > i")
    MY_RECORDS_BTN = (By.CSS_SELECTOR, "reports-nav > div > ul > li:nth-child(1) > a > div > i")
    RECORDINGS_BTN = (By.CSS_SELECTOR, "reports-nav > div > ul > li:nth-child(2) > a > div > i")
    DEALS_BTN = (By.CSS_SELECTOR, " reports-nav > div > ul > li:nth-child(3) > a.flex-center-center > div")
    COACHING_BTN = (By.CSS_SELECTOR, "reports-nav > div > ul > li:nth-child(4) > a > i")
    ANALYSIS_BTN = (By.CSS_SELECTOR, "reports-nav > div > ul > li:nth-child(5) > a > div > i")
    PLAYLIST_BTN = (By.CSS_SELECTOR, "reports-nav > div > ul > li:nth-child(6) > a > div > i")
