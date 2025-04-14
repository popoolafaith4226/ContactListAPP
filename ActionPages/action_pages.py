import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Loginlocators.locator import Click_signup_button, Login_locators, Add_new_contact


class signup_button:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        click_the_signup_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Signup_button))
        click_the_signup_button.click()
        time.sleep(3)

class first_name:
    def __init__(self, driver):
        self.driver = driver

    def input_first_name(self, user_first_name):
        click_firstname_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Firstname_field))
        click_firstname_field.send_keys(user_first_name)
        time.sleep(3)

class last_name:
    def __init__(self, driver):
        self.driver = driver

    def input_last_name(self,user_last_name):
        input_last_name= WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Lastname_field))
        input_last_name.send_keys(user_last_name)
        time.sleep(3)


class email:
    def __init__(self, driver):
        self.driver = driver

    def input_email(self, user_email):
        input_last_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Email_field))
        input_last_name.send_keys(user_email)
        time.sleep(3)

class password:
    def __init__(self, driver):
        self.driver = driver

    def input_password(self, user_password):
        input_the_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Password_field))
        input_the_password.send_keys(user_password)
        time.sleep(3)

class submit_button:
    def __init__(self, driver):
        self.driver = driver

    def click_submit_button(self):
        click_the_submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Click_signup_button.Submit_button))
        click_the_submit_button.click()
        time.sleep(3)

class Add_contact_button:
    def __init__(self, driver):
        self.driver = driver

    def click_add_contact_button(self):
        click_contact_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Click_contact_button))
        click_contact_button.click()
        time.sleep(3)

class Add_contact_first_name:
    def __init__(self, driver):
        self.driver = driver


    def Contact_first_name(self, add_firstname):
        input_contact_firstname = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_first_name))
        input_contact_firstname.send_keys(add_firstname)
        time.sleep(3)

class Add_contact_last_name:
    def __init__(self, driver):
        self.driver = driver

    def Contact_last_name(self, add_lastname):
        input_contact_firstname = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_last_name))
        input_contact_firstname.send_keys(add_lastname)
        time.sleep(3)

class Add_contact_DOB:
    def __init__(self, driver):
        self.driver = driver


    def Contact_dateofbirth(self, add_birthdate):
        input_contact_birthdate = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_DOB))
        input_contact_birthdate.send_keys(add_birthdate)
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