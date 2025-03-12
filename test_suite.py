import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from ActionPages.action_pages import login_pages, signup_button
from Config.config import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
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

def test_sign_up_page(signup):
    the_signup_button = signup_button(signup.driver)
    the_signup_button.click_signup_button()

