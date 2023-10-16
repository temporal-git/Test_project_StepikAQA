from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        self.find_element_and_click(BasketPageLocators.TOP_BASKET_BUTTON)

    def check_is_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BY), "The basket does not empty"

    def check_text_is_basket_empty(self):
        expected_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert expected_text == "Your basket is empty. Continue shopping", "The text about the basket being empty is missing."
