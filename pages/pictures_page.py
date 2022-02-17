from .base_page import BasePage
from .locators import PicturesPageLocators


class PicturesPage(BasePage):
    def add_to_cart(self):
        add_button=self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price



    def get_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return name

    def basket_validation(self, e_name, e_price):
        a_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        a_price = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text
        assert e_name == a_name, \
            f'Wrong product name in basket. Expected {e_name}, got {a_name}'
        assert e_price == a_price, \
            f'Basket value not match product price. Expected {e_price}, got {a_price}'

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_form()
        self.should_be_product_form()

    def should_be_product_url(self):
        assert 'catalogue' in self.browser.current_url,\
            'Seems that URL is not catalogue URL'

    def should_be_add_to_basket_form(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_FORM),\
            'Seems that add-to-basket form is missing from product page'

    def should_be_product_form(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_FORM),\
            'Seems that product form is missing from product page'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_TO_BASKET_CONFIRM),\
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_CONFIRM), \
            "Success message is presented, but should disappear"
