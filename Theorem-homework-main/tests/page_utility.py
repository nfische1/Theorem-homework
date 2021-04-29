import random
import string

from page_locators import AccountCreationPageLocators, LoginPageLocators
import screenshots
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    default_wait = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_visibility(self, by_locator, timeout=default_wait):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator))

    def wait_for_element_invisibility(self, by_locator, timeout=default_wait):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(by_locator))

    def wait_for_element_presence(self, by_locator, timeout=default_wait):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))

    def click_element(self, by_locator):
        self.wait_for_element_visibility(by_locator)
        element = self.driver.find_element(*by_locator)
        element.click()

    def element_is_displayed(self, by_locator):
        """This method is specifically useful when checking for an element that DOESNT/SHOULDNT exist.
        If you simply call .is_displayed() you get an exception error, this handles it"""
        try:
            # Element is found so return TRUE
            return self.driver.find_element(*by_locator).is_displayed()
        except NoSuchElementException:
            # Element not found and raises exception, return FALSE
            return False

    def enter_text(self, by_locator, text_to_enter):
        self.wait_for_element_visibility(by_locator)
        element = self.driver.find_element(*by_locator)
        element.clear()
        element.send_keys(text_to_enter)

    def random_string(self, stringLength=10):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength)).lower()

    def random_number(self, range=10):
        amount = random.randrange(range)
        if amount < 1:
            amount = amount + 1
        return amount


class AccountCreation(BasePage):

    def wait_for_load_complete(self):
        self.wait_for_element_visibility(*LoginPageLocators.LOGIN_BUTTON)
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_element_visibility(*AccountCreationPageLocators.CREATE_ACCOUNT_BTN)
        screenshots.take_screenshot(self.driver, 'Account Creation Page')

    def account_creation_page(self):
        self.wait_for_element_visibility(*AccountCreationPageLocators.CREATE_ACCOUNT_BTN)
        screenshots.take_screenshot(self.driver, 'Account Creation Page')

    def enter_new_account_email(self, email):
        self.click_element(*AccountCreationPageLocators.EMAIL_ADDRESS_FIELD)
        self.enter_text(*AccountCreationPageLocators.EMAIL_ADDRESS_FIELD, email)

    def create_an_account_page(self):
        self.wait_for_element_visibility(*AccountCreationPageLocators.PAGE_HEADING)



class Login(BasePage):

    def login_page(self):
        self.wait_for_element_visibility(self.wait_for_element_visibility(*LoginPageLocators.LOGIN_BUTTON))
        self.click_element(*LoginPageLocators.LOGIN_BUTTON)
