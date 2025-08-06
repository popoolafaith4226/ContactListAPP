import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Loginlocators.locator import Click_signup_button, Login_locators, Add_new_contact

#login
class LoginPages:
    def __init__(self,driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, user_name):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.USERNAME))
        username.send_keys(user_name)

    def enter_password(self, user_password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.PASSWORD))
        enter_password.send_keys(user_password)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Login_locators.LOGIN_BUTTON))
        click_login_button.click()

class SignupButton:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button(self):
        click_the_signup_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Signup_button))
        click_the_signup_button.click()
        time.sleep(3)

class FirstName:
    def __init__(self, driver):
        self.driver = driver

    def input_first_name(self, user_first_name):
        click_firstname_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Firstname_field))
        click_firstname_field.send_keys(user_first_name)
        time.sleep(3)

class LastName:
    def __init__(self, driver):
        self.driver = driver

    def input_last_name(self,user_last_name):
        input_last_name= WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Lastname_field))
        input_last_name.send_keys(user_last_name)
        time.sleep(3)


class Email:
    def __init__(self, driver):
        self.driver = driver

    def input_email(self, user_email):
        input_last_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Email_field))
        input_last_name.send_keys(user_email)
        time.sleep(3)

class Password:
    def __init__(self, driver):
        self.driver = driver

    def input_password(self, user_password):
        input_the_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(Click_signup_button.Password_field))
        input_the_password.send_keys(user_password)
        time.sleep(3)

class SubmitButton:
    def __init__(self, driver):
        self.driver = driver

    def click_submit_button(self):
        click_the_submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Click_signup_button.Submit_button))
        click_the_submit_button.click()
        time.sleep(3)

class AddContactButton:
    def __init__(self, driver):
        self.driver = driver

    def click_add_contact_button(self):
        click_contact_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Click_contact_button))
        click_contact_button.click()
        time.sleep(3)

class AddContactFirstName:
    def __init__(self, driver):
        self.driver = driver


    def contact_first_name(self, add_firstname):
        input_contact_firstname = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_first_name))
        input_contact_firstname.send_keys(add_firstname)
        time.sleep(3)

class AddContactLastName:
    def __init__(self, driver):
        self.driver = driver

    def contact_last_name(self, add_lastname):
        input_contact_firstname = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_last_name))
        input_contact_firstname.send_keys(add_lastname)
        time.sleep(3)

class AddContactDOB:
    def __init__(self, driver):
        self.driver = driver


    def contact_date_of_birth(self, add_birthdate):
        input_contact_birthdate = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_DOB))
        input_contact_birthdate.send_keys(add_birthdate)
        time.sleep(3)

class AddContactEmail:
    def __init__(self, driver):
        self.driver = driver

    def contact_email(self, add_email):
        input_contact_email = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_Email))
        input_contact_email.send_keys(add_email)
        time.sleep(3)

class AddContactPhone:
    def __init__(self, driver):
        self.driver = driver

    def contact_phone(self, add_phone):
        input_contact_phone = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_phone))
        input_contact_phone.send_keys(add_phone)
        time.sleep(3)

class AddContactAddress1:
    def __init__(self, driver):
        self.driver = driver

    def contact_address1(self, add_address1):
        input_contact_address1 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_Street_address1))
        input_contact_address1.send_keys(add_address1)
        time.sleep(3)

class AddContactAddress2:
    def __init__(self, driver):
        self.driver = driver

    def contact_address2(self, add_address2):
        input_contact_address2 = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_Street_address2))
        input_contact_address2.send_keys(add_address2)
        time.sleep(3)


class AddContactCity:
    def __init__(self, driver):
        self.driver = driver

    def contact_city(self, add_city):
        input_contact_city = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_city))
        input_contact_city.send_keys(add_city)
        time.sleep(3)

class AddContactState:
    def __init__(self, driver):
        self.driver = driver

    def contact_state(self, add_state):
        input_contact_city = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_State))
        input_contact_city.send_keys(add_state)
        time.sleep(3)

class AddContactPostalCode:
    def __init__(self, driver):
        self.driver = driver

    def contact_postal_code(self, add_postalcode):
        input_contact_postalcode = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_Postalcode))
        input_contact_postalcode.send_keys(add_postalcode)
        time.sleep(3)

class AddContactCountry:
    def __init__(self, driver):
        self.driver = driver

    def contact_country(self, add_country):
        input_contact_country = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_Country))
        input_contact_country.send_keys(add_country)
        time.sleep(3)

class CLickSubmitButton:
    def __init__(self, driver):
        self.driver = driver

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_submit_button))
        click_submit_button.click()
        time.sleep(3)



class LogOutButton:
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        click_logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(Add_new_contact.Contact_logout_button))
        click_logout_button.click()
        time.sleep(3)
