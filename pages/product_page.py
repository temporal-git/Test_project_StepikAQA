from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        basket_button.click()

    def should_add_prodict_successful(self):
        self.is_element_present(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL)
        self.should_notice_content_product_success_message()
        self.should_total_price_go_up()

    def should_notice_content_product_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME_PRODUCT).text
        assert alert_name == product_name, "Wrong successful notice text"

    def should_total_price_go_up(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price in basket_total, "The total price does not go up"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_element_disappeared(*ProductPageLocators.NOTICE_PRODUCT_ADD_SUCCESSFUL), \
            "Success message is not disappeared"
