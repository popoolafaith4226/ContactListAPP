from selenium.webdriver.common.by import By


class Login_locators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class Click_signup_button:
    Signup_button = (By.XPATH, "//*[@id='signup']")

