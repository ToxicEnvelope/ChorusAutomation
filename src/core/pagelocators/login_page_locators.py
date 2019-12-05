from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "form > button")
    CONTINUE_BTN = (By.CSS_SELECTOR, "button.email")
