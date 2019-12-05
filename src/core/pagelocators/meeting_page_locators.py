from selenium.webdriver.common.by import By

class MeetingPageLocators:
    BACKWARDS_BTN = (By.CSS_SELECTOR, "div:nth-child(1) > i.fa-back-15")
    PLAY_BTN = (By.CSS_SELECTOR, "div:nth-child(2) > i.fa-play")
    PAUSE_BTN = (By.CSS_SELECTOR, "div:nth-child(2) > i.fa-pause")
    FORWARDS_BTN = (By.CSS_SELECTOR, "div:nth-child(3) > i.fa-forward-15")
    DURATION_TEXT = (By.CSS_SELECTOR, "div > span > span.duration")
