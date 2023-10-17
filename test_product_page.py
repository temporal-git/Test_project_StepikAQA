from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
from faker import Faker


@pytest.mark.need_review
@pytest.mark.parametrize('number', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    # проверяет, что гость может добавить товар в корзину
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{number}"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_notice_content_product_success_message()
    prod_page.should_add_prodict_successful()


def test_guest_can_add_product_to_basket_one_link(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_add_prodict_successful()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    # проверяет, что гость не видит сообщения об успешном добавлении
    # товара после его добавления в корзину
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    # проверяет, что при открытии страницы гость не видит сообщения
    # об успешном добавлении товара в корзину
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    # проверяет, что сообщение об успешном добавлении товара в корзину
    # исчезает спустя некоторое время
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_product_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    # гость должен увидеть ссылку для входа на странице продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    # гость может перейти на страницу авторизации со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # проверяет, что в корзине нет товаров при переходе в нее со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket = BasketPage(browser, browser.current_url)
    basket.go_to_basket_page()
    basket.check_is_basket_is_empty()
    basket.check_text_is_basket_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # выполняется перед запуском каждого теста, принадлежащего данному классу
        # регистрирует нового пользователя
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        email = Faker().email()
        password = Faker().passport_number() + "!"
        login = LoginPage(browser, link)
        login.open()
        login.register_new_user(email, password)
        login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # проверяет, что при открытии страницы пользователь не видит сообщения
        # об успешном добавлении товара в корзину
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        # проверяет, что пользователь может добавить товар в корзину
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_success_message()
        prod_page.add_product_to_basket()
        prod_page.solve_quiz_and_get_code()
        prod_page.should_add_prodict_successful()
