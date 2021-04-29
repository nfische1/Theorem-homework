import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

from tests import screenshots
from tests.page_locators import LoginPageLocators, AccountCreationPageLocators


class BasePage(object):
    default_wait = 300

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


class AccountCreationPage(BasePage):

    def navigate_to_account_creation(self):
        self.wait_for_element_visibility(LoginPageLocators.LOGIN_BUTTON)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_element_visibility(AccountCreationPageLocators.CREATE_ACCOUNT_BTN)
        screenshots.take_screenshot(self.driver, 'Account Creation Page')

    def wait_for_load_complete(self):
        self.wait_for_element_visibility(AccountCreationPageLocators.CREATE_ACCOUNT_BTN)
        screenshots.take_screenshot(self.driver, 'Account Creation Page')

    def enter_new_account_email(self, email):
        self.click_element(AccountCreationPageLocators.EMAIL_ADDRESS_FIELD)
        self.enter_text(AccountCreationPageLocators.EMAIL_ADDRESS_FIELD, email)
        self.click_element(AccountCreationPageLocators.CREATE_ACCOUNT_BTN)

    def enter_first_name(self, first_name):
        self.click_element(AccountCreationPageLocators.FIRST_NAME_FIELD)
        self.enter_text(AccountCreationPageLocators.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.click_element(AccountCreationPageLocators.LAST_NAME_FIELD)
        self.enter_text(AccountCreationPageLocators.LAST_NAME_FIELD, last_name)

    def enter_password(self, password):
        self.click_element(AccountCreationPageLocators.PASSWORD_FIELD)
        self.enter_text(AccountCreationPageLocators.PASSWORD_FIELD, password)

    def enter_date_of_birth(self, day, month, year):
        # Day of Birth
        self.wait_for_element_visibility(AccountCreationPageLocators.BIRTH_DAY_DROPDOWN)
        self.click_element(AccountCreationPageLocators.BIRTH_DAY_DROPDOWN)
        option_list = self.driver.find_elements(AccountCreationPageLocators.OPTION)
        for option in option_list:
            print("this is option" + str(option))
            if option.text.__contains__(day):
                option.click()
                time.sleep(1)
                break
        # Month of Birth
        self.wait_for_element_visibility(AccountCreationPageLocators.BIRTH_MONTH_DROPDOWN)
        self.click_element(AccountCreationPageLocators.BIRTH_MONTH_DROPDOWN)
        option_list = self.driver.find_elements(AccountCreationPageLocators.OPTION)
        for option in option_list:
            print("this is option" + str(option))
            if option.text.__contains__(month):
                option.click()
                time.sleep(1)
                break
        # Year of birth
        self.wait_for_element_visibility(AccountCreationPageLocators.BIRTH_YEAR_DROPDOWN)
        self.click_element(AccountCreationPageLocators.BIRTH_YEAR_DROPDOWN)
        option_list = self.driver.find_elements(AccountCreationPageLocators.OPTION)
        for option in option_list:
            print("this is option" + str(option))
            if option.text.__contains__(year):
                option.click()
                time.sleep(1)
                break

    def enter_address(self, address):
        self.wait_for_element_visibility(AccountCreationPageLocators.ADDRESS_FIELD)
        self.click_element(AccountCreationPageLocators.ADDRESS_FIELD)
        self.enter_text(AccountCreationPageLocators.ADDRESS_FIELD, address)

    def enter_city(self, city):
        self.wait_for_element_visibility(AccountCreationPageLocators.CITY_FIELD)
        self.click_element(AccountCreationPageLocators.CITY_FIELD)
        self.enter_text(AccountCreationPageLocators.CITY_FIELD, city)

    def enter_state(self, state):
        self.wait_for_element_visibility(AccountCreationPageLocators.STATE_DROPDOWN)
        self.click_element(AccountCreationPageLocators.STATE_DROPDOWN)
        self.enter_text(AccountCreationPageLocators.STATE_DROPDOWN, state)
        self.click_element(AccountCreationPageLocators.OPTION)

    def enter_zipcode(self, zip):
        self.wait_for_element_visibility(AccountCreationPageLocators.ZIPCODE_FIELD)
        self.click_element(AccountCreationPageLocators.ZIPCODE_FIELD)
        self.enter_text(AccountCreationPageLocators.ZIPCODE_FIELD, zip)

    def enter_country(self, country):
        self.wait_for_element_visibility(AccountCreationPageLocators.COUNTRY_DROPDOWN)
        self.click_element(AccountCreationPageLocators.COUNTRY_DROPDOWN)
        self.enter_text(AccountCreationPageLocators.COUNTRY_DROPDOWN, country)
        self.click_element(AccountCreationPageLocators.OPTION)

    def enter_mobile_phone(self, mobile):
        self.wait_for_element_visibility(AccountCreationPageLocators.MOBILE_PHONE)
        self.click_element(AccountCreationPageLocators.MOBILE_PHONE)
        self.enter_text(AccountCreationPageLocators.MOBILE_PHONE, mobile)

    def enter_address_alias(self, alias):
        self.wait_for_element_visibility(AccountCreationPageLocators.ADDRESS_ALIAS)
        self.click_element(AccountCreationPageLocators.ADDRESS_ALIAS)
        self.enter_text(AccountCreationPageLocators.ADDRESS_ALIAS, alias)

    def click_register(self):
        self.wait_for_element_visibility(AccountCreationPageLocators.REGISTER_BUTTON)
        self.click_element(AccountCreationPageLocators.REGISTER_BUTTON)


class Login(BasePage):

    def login_page(self, email, password):
        self.wait_for_element_visibility(LoginPageLocators.LOGIN_BUTTON)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

