import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Loginlocators.locator import Click_signup_button


class signup_button:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        click_the_signup_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Signup_button))
        click_the_signup_button.click()
        time.sleep(3)



class login_pages:
    def __init__(self,driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_firstname(self, user_name):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.USERNAME))
        username.send_keys(user_name)