import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from ActionPages.action_pages import LoginPages, SignupButton,  \
    AddContactButton,  LogOutButton
from Config.config import Config

# @pytest.fixture(scope="module")
# def driver_setup():
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
#     chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(30)
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.fixture(scope="module")
def driver_setup():
    # Uncomment the browser you want to use

    # Chrome
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    # chrome_options.add_argument("--disable-gpu")
    # driver = webdriver.Chrome(options=chrome_options)

    # Firefox
    firefox_options = FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)

    # # Edge
    # edge_options = EdgeOptions()
    # driver = webdriver.Edge(options=edge_options)

    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")

def signup(driver_setup):
    driver = driver_setup
    login_page = LoginPages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page

   # login screen
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPages(driver)
    login_page.login_url(Config.BASEURL)
    return login_page


def test_sign_up_page(signup):
    the_signup_button = SignupButton(signup.driver)
    the_signup_button.click_signup_button()

def test_first_name(signup):
    the_firstname_field = SignupButton(signup.driver)
    the_firstname_field.input_first_name(Config.FIRSTNAME)

# test the lastname
def test_last_name(signup):
    the_lastname_field = SignupButton(signup.driver)
    the_lastname_field.input_last_name(Config.LASTNAME)

def test_email_field(signup):
    the_email_field = SignupButton(signup.driver)
    the_email_field.input_email(Config.EMAIL)

def test_password_field(signup):
    the_password_field = SignupButton(signup.driver)
    the_password_field.input_password(Config.PASSWORD)

def test_submit_signup_button(signup):
    the_submit_button = SignupButton(signup.driver)
    the_submit_button.click_submit_button()

def test_add_contact_button(signup):
    the_add_contact_button = AddContactButton(signup.driver)
    the_add_contact_button.click_add_contact_button()

def test_contact_firstname(signup):
    the_firstname_field = AddContactButton(signup.driver)
    the_firstname_field.contact_first_name(Config.CONTACT_FIRSTNAME)

def test_contact_lastname(signup):
    the_lastname_field = AddContactButton(signup.driver)
    the_lastname_field.contact_last_name(Config.CONTACT_LASTNAME)

def test_contact_dob(signup):
    the_dob_field = AddContactButton(signup.driver)
    the_dob_field.contact_date_of_birth(Config.CONTACT_DATE_OF_BIRTH)

def test_contact_email(signup):
    the_email_field = AddContactButton(signup.driver)
    the_email_field.contact_email(Config.CONTACT_EMAIL)

def test_contact_phone(signup):
    the_phone_field = AddContactButton(signup.driver)
    the_phone_field.contact_phone(Config.CONTACT_PHONE)

def test_contact_address1(signup):
    the_address1_field = AddContactButton(signup.driver)
    the_address1_field.contact_address1(Config.CONTACT_ADDRESS_1)

def test_contact_address2(signup):
    the_address2_field = AddContactButton(signup.driver)
    the_address2_field.contact_address2(Config.CONTACT_ADDRESS_2)

def test_contact_city(signup):
    the_city_field = AddContactButton(signup.driver)
    the_city_field.contact_city(Config.CONTACT_CITY)

def test_contact_state(signup):
    the_state_field = AddContactButton(signup.driver)
    the_state_field.contact_state(Config.CONTACT_STATE)

def test_contact_postalcode(signup):
    the_postalcode_field = AddContactButton(signup.driver)
    the_postalcode_field.contact_postal_code(Config.CONTACT_POSTCODE)


def test_contact_country(signup):
    the_country_field = AddContactButton(signup.driver)
    the_country_field.contact_country(Config.CONTACT_COUNTRY)

def test_submit_button(signup):
    the_submit_button = AddContactButton(signup.driver)
    the_submit_button.click_submit_button()


@pytest.mark.parametrize("iteration", range(10))
def test_complete_contact_flow(signup, iteration):
    """Complete contact creation flow - runs 10 times"""

    # Add contact button
    the_add_contact_button = AddContactButton(signup.driver)
    the_add_contact_button.click_add_contact_button()

    # First name
    the_firstname_field = AddContactButton(signup.driver)
    the_firstname_field.contact_first_name(Config.CONTACT_FIRSTNAME)

    # Last name
    the_lastname_field = AddContactButton(signup.driver)
    the_lastname_field.contact_last_name(Config.CONTACT_LASTNAME)

    # Date of birth
    the_dob_field = AddContactButton(signup.driver)
    the_dob_field.contact_date_of_birth(Config.CONTACT_DATE_OF_BIRTH)

    # Email
    the_email_field = AddContactButton(signup.driver)
    the_email_field.contact_email(Config.CONTACT_EMAIL)

    # Phone
    the_phone_field = AddContactButton(signup.driver)
    the_phone_field.contact_phone(Config.CONTACT_PHONE)

    # Address 1
    the_address1_field = AddContactButton(signup.driver)
    the_address1_field.contact_address1(Config.CONTACT_ADDRESS_1)

    # Address 2
    the_address2_field = AddContactButton(signup.driver)
    the_address2_field.contact_address2(Config.CONTACT_ADDRESS_2)

    # City
    the_city_field = AddContactButton(signup.driver)
    the_city_field.contact_city(Config.CONTACT_CITY)

    # State
    the_state_field = AddContactButton(signup.driver)
    the_state_field.contact_state(Config.CONTACT_STATE)

    # Postal code
    the_postalcode_field = AddContactButton(signup.driver)
    the_postalcode_field.contact_postal_code(Config.CONTACT_POSTCODE)

    # Country
    the_country_field = AddContactButton(signup.driver)
    the_country_field.contact_country(Config.CONTACT_COUNTRY)

    # Submit
    the_submit_button = AddContactButton(signup.driver)
    the_submit_button.click_submit_button()


def test_logout_button(signup):
    the_logout_button = LogOutButton(signup.driver)
    the_logout_button.click_logout_button()

def test_username(signup):
    the_username_field = LoginPages(signup.driver)
    the_username_field.enter_username(Config.LOGIN_USERNAME)

def test_password(signup):
    the_password_field = LoginPages(signup.driver)
    the_password_field.enter_password(Config.LOGIN_PASSWORD)

def test_login_button (signup):
    click_the_login_button = LoginPages(signup.driver)
    click_the_login_button.click_login_button()

    # logout
    the_logout_button = LogOutButton(signup.driver)
    the_logout_button.click_logout_button()