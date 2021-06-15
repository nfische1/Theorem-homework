from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests import gen_rand_value, page_utility, screenshots


def test_create_account():
    # Setup Driver, define options
    options = Options()
    # Comment out the line below if you want to see the test run on a web page
    # options.add_argument('--headless')
    options.add_argument('--window-size=2600,9000')
    driver = webdriver.Chrome(options=options)
    driver.get("http://automationpractice.com")
    # Users and Pages defined
    first_name = 'Account' + gen_rand_value.random_string(5)
    last_name = 'CreationTest' + gen_rand_value.random_string(5)
    email = first_name.replace(' ', '_') + '@' + last_name.replace(' ', '_') + '.org'
    password = 'testpw' + str(gen_rand_value.random_number(2))
    create_account = page_utility.AccountCreationPage(driver)
    address = str(gen_rand_value.random_number(3)) + ' West ' + gen_rand_value.random_string(6) + ' Circle'
    city = gen_rand_value.random_string(3)
    state = 'Utah'
    zipcode = gen_rand_value.random_number(5)
    country = 'United States'
    mobile = str(gen_rand_value.random_number(3)) + '-' + str(gen_rand_value.random_number(
        3)) + '-' + str(gen_rand_value.random_number(4))
    screenshots.take_screenshot(driver, 'Main Page')
    create_account.navigate_to_account_creation()
    create_account.wait_for_load_complete()
    # Fill out initial email
    screenshots.take_screenshot(driver, 'Enter email for account creation/ login page')
    create_account.enter_new_account_email(email)
    # Fill out form
    screenshots.take_screenshot(driver, 'Super long account creation form')
    create_account.enter_first_name(first_name)
    create_account.enter_last_name(last_name)
    create_account.enter_password(password)
    create_account.enter_address(address)
    create_account.enter_city(city)
    screenshots.take_screenshot(driver, 'This is as far as time would allow')
    driver.quit()
