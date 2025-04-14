from selenium.webdriver.common.by import By


class Login_locators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

class Click_signup_button:
    Signup_button = (By.XPATH, "//*[@id='signup']")
    Firstname_field = (By.XPATH, "//*[@id='firstName']")
    Lastname_field = (By.XPATH, '//*[@id="lastName"]')
    Email_field = (By.XPATH, '//*[@id="email"]')
    Password_field = (By.XPATH, '//*[@id="password"]')
    Submit_button = (By.XPATH, '//*[@id="submit"]')

class Add_new_contact:
    Click_contact_button = (By.XPATH, '//*[@id="add-contact"]')
    Contact_first_name = (By.XPATH, '//*[@id="firstName"]')
    Contact_last_name = (By.XPATH, '//*[@id="lastName"]')
    Contact_DOB = (By.XPATH, '//*[@id="birthdate"]')
    Contact_Email = (By.XPATH, '//*[@id="email"]')
    Contact_phone = (By.XPATH, '//*[@id="phone"]')
    Contact_Street_address1 = (By.XPATH, '//*[@id="street1"]')
    Contact_Street_address2 = (By.XPATH, '//*[@id="street2"]')
    Contact_city = (By.XPATH, '//*[@id="city"]')
    Contact_State = (By.XPATH, '//*[@id="stateProvince"]')
    Contact_Postalcode = (By.XPATH, '//*[@id="postalCode"]')
    Contact_Country = (By.XPATH, '//*[@id="country"]')
    Contact_submit_button = (By.XPATH, '//*[@id="submit"]')




