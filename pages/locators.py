from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_FORM_LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTERED_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTERED_FORM_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTERED_FORM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTERED_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTERED_FORM_REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")