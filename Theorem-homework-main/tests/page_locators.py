from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """Base Page Locators - Elements on EVERY page"""
    CONTACT_US = (By.ID, "contact-link")
    CART = (By.CSS_SELECTOR, "[class='shopping_cart']")


class AccountCreationPageLocators(object):
    """A class for Account Creation page locators."""
    EMAIL_ADDRESS_FIELD = (By.ID, "[id='email_create']")
    CREATE_ACCOUNT_BTN = (By.ID, "[id='create_account_form']")
    ERROR = (By.ID, "[id='create_account_error']")
    MR_RADIO = (By.ID, "[id='uniform-id_gender1']")
    MRS_RADIO = (By.ID, "[id='uniform-id_gender2']")
    PAGE_HEADING = (By.ID, "page-heading")
    PAGE_SUBHEADING = (By.ID, "page-subheading")
    FIRST_NAME_FIELD = (By.ID, "[id='customer_firstname']")
    LAST_NAME_FIELD = (By.ID, "[id='customer_lastname']")
    FORM_EMAIL_ADDRESS = (By.ID, "[id='email']")
    PASSWORD_FIELD = (By.ID, "[id='passwd']")
    BIRTH_DAY_DROPDOWN = (By.ID, "[id='days']")
    BIRTH_MONTH_DROPDOWN = (By.ID, "[id='months']")
    BIRTH_YEAR_DROPDOWN = (By.ID, "[id='years']")
    NEWS_LETTER_BOX = (By.ID, "[id='newsletter']")
    SPECIAL_OFFERS_BOX = (By.ID, "[id='uniform-optin']")
    COMPANY_FIELD = (By.ID, "[id='company']")
    ADDRESS_FIELD = (By.ID, "[id='address1']")
    ADDRESS_LINE2_FIELD = (By.ID, "[id='address2']")
    CITY_FIELD = (By.ID, "[id='city']")
    STATE_DROPDOWN = (By.ID, "[id='id_state']")
    ZIPCODE_FIELD = (By.ID, "[id='postcode']")
    COUNTRY_DROPDOWN = (By.ID, "[id='id_country']")
    ADDITIONAL_INFORMATION = (By.ID, "[id='other']")
    HOME_PHONE = (By.ID, "[id='phone']")
    MOBILE_PHONE = (By.ID, "[id='phone_mobile']")
    ADDRESS_ALIAS = (By.ID, "[id='alias']")
    REGISTER_BUTTON = (By.ID, "[id='submitAccount']")
    OPTION = (By.TAG_NAME, "OPTION")


class LoginPageLocators(object):
    """A class for Login page locators."""
    LOGIN_BUTTON = (By.CLASS_NAME, "login")
    SIGN_OUT_BUTTON = (By.CLASS_NAME, "logout")
