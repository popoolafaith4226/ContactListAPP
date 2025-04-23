import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPages.action_pages import login_pages, signup_button, first_name, last_name, email, password, submit_button, \
    Add_contact_button, Add_contact_first_name, Add_contact_last_name, Add_contact_DOB, Add_contact_email, \
    Add_contact_phone, AddContactAddress1, AddContactCity, AddContactState, AddContactCountry, CLickSubmitButton, \
    AddContactAddress2, AddContactPostalCode
from Config.config import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")

def signup(driver_setup):
    driver = driver_setup
    login_page = login_pages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page

def login(driver_setup):
    driver = driver_setup
    login_page = login_pages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page
#
# def test_username(signup):
#     the_username_field = login_pages(signup.driver)
#     the_username_field.enter_username(Config.LOGIN_USERNAME)
#
# def test_password(signup):
#     the_password_field = login_pages(signup.driver)
#     the_password_field.enter_password(Config.LOGIN_PASSWORD)
#
# def test_login_button (signup):
#     click_the_login_button = login_pages(signup.driver)
#     click_the_login_button.click_login_button()

def test_sign_up_page(signup):
    the_signup_button = signup_button(signup.driver)
    the_signup_button.click_signup_button()

def test_first_name(signup):
    the_firstname_field = first_name(signup.driver)
    the_firstname_field.input_first_name(Config.FIRSTNAME)

def test_last_name(signup):
    the_lastname_field = last_name(signup.driver)
    the_lastname_field.input_last_name(Config.LASTNAME)

def test_email_field(signup):
    the_email_field = email(signup.driver)
    the_email_field.input_email(Config.EMAIL)

def test_password_field(signup):
    the_password_field = password(signup.driver)
    the_password_field.input_password(Config.PASSWORD)

def test_submit_signup_button(signup):
    the_submit_button = submit_button(signup.driver)
    the_submit_button.click_submit_button()

def test_add_contact_button(signup):
    the_add_contact_button = Add_contact_button(signup.driver)
    the_add_contact_button.click_add_contact_button()

def test_contact_firstname(signup):
    the_firstname_field = Add_contact_first_name(signup.driver)
    the_firstname_field.Contact_first_name(Config.CONTACT_FIRSTNAME)

def test_contact_lastname(signup):
    the_lastname_field = Add_contact_last_name(signup.driver)
    the_lastname_field.Contact_last_name(Config.CONTACT_LASTNAME)

def test_contact_dob(signup):
    the_dob_field = Add_contact_DOB(signup.driver)
    the_dob_field.Contact_dateofbirth(Config.CONTACT_DATE_OF_BIRTH)

def test_contact_email(signup):
    the_email_field = Add_contact_email(signup.driver)
    the_email_field.Contact_email(Config.CONTACT_EMAIL)

def test_contact_phone(signup):
    the_phone_field = Add_contact_phone(signup.driver)
    the_phone_field.contact_phone(Config.CONTACT_PHONE)

def test_contact_address1(signup):
    the_address1_field = AddContactAddress1(signup.driver)
    the_address1_field.contact_address1(Config.CONTACT_ADDRESS_1)

def test_contact_address2(signup):
    the_address2_field = AddContactAddress2(signup.driver)
    the_address2_field.contact_address2(Config.CONTACT_ADDRESS_2)

def test_contact_city(signup):
    the_city_field = AddContactCity(signup.driver)
    the_city_field.contact_city(Config.CONTACT_CITY)

def test_contact_state(signup):
    the_state_field = AddContactState(signup.driver)
    the_state_field.contact_state(Config.CONTACT_STATE)

def test_contact_postalcode(signup):
    the_postalcode_field = AddContactPostalCode(signup.driver)
    the_postalcode_field.contact_postal_code(Config.CONTACT_POSTCODE)


def test_contact_country(signup):
    the_country_field = AddContactCountry(signup.driver)
    the_country_field.contact_country(Config.CONTACT_COUNTRY)

def test_submit_button(signup):
    the_submit_button = CLickSubmitButton(signup.driver)
    the_submit_button.click_submit_button()