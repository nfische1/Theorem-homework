from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """Base Page Locators - Elements on EVERY page"""
    CONTACT_US = (By.ID, "contact-link")
    CART = (By.CSS_SELECTOR, "[class='shopping_cart']")


class AccountCreationPageLocators(object):
    """A class for Account Creation page locators."""
    EMAIL_ADDRESS_FIELD = (By.ID, 'email_create')
    CREATE_ACCOUNT_BTN = (By.ID, 'SubmitCreate')
    ERROR = (By.ID, 'create_account_error')
    MR_RADIO = (By.ID, 'uniform-id_gender1')
    MRS_RADIO = (By.ID, 'uniform-id_gender2')
    PAGE_HEADING = (By.ID, "page-heading")
    PAGE_SUBHEADING = (By.ID, "page-subheading")
    FIRST_NAME_FIELD = (By.ID, 'customer_firstname')
    LAST_NAME_FIELD = (By.ID, 'customer_lastname')
    FORM_EMAIL_ADDRESS = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'passwd')
    BIRTH_DAY_DROPDOWN = (By.ID, 'days')
    BIRTH_MONTH_DROPDOWN = (By.ID, 'months')
    BIRTH_YEAR_DROPDOWN = (By.ID, 'years')
    NEWS_LETTER_BOX = (By.ID, "[id='newsletter']")
    SPECIAL_OFFERS_BOX = (By.ID, 'uniform-optin')
    COMPANY_FIELD = (By.ID, 'company')
    ADDRESS_FIELD = (By.ID, 'address1')
    ADDRESS_LINE2_FIELD = (By.ID, 'address2')
    CITY_FIELD = (By.ID, 'city')
    STATE_DROPDOWN = (By.ID, 'id_state')
    ZIPCODE_FIELD = (By.ID, 'postcode')
    COUNTRY_DROPDOWN = (By.ID, 'id_country')
    ADDITIONAL_INFORMATION = (By.ID, 'other')
    HOME_PHONE = (By.ID, 'phone')
    MOBILE_PHONE = (By.ID, 'phone_mobile')
    ADDRESS_ALIAS = (By.ID, 'alias')
    REGISTER_BUTTON = (By.ID, 'submitAccount')
    OPTION = (By.TAG_NAME, "OPTION")


class LoginPageLocators(object):
    """A class for Login Logout page locators."""
    HEADER_INFO = (By.CSS_SELECTOR, "[class='header_user_info]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[class='login']")
    SIGN_OUT_BUTTON = (By.CLASS_NAME, "logout")
