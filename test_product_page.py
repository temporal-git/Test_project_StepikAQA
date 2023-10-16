from .pages.product_page import ProductPage
import pytest


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket_10_links(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_add_prodict_successful()


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_add_prodict_successful()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_disappeared_success_message()
