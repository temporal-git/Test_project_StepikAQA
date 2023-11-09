from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == LoginPageLocators.LOGIN_URL, "Wrong Login page URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form does not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTERED_FORM), "The registered form does not present"

    def register_new_user(self, email, password):
        # Method for user's registration.
        email_field = self.browser.find_element(*LoginPageLocators.REGISTERED_FORM_EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTERED_FORM_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTERED_FORM_PASSWORD_CONFIRM)
        confirm_password_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTERED_FORM_REGISTER_BUTTON)
        submit_button.click()

#git commit
