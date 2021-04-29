
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests import web_app_setup, gen_rand_value, page_utility


def test_create_account():
    # Setup Driver, define options
    options = Options()
    # Comment out the line below if you want to see the test run
    # options.add_argument('--headless')
    options.add_argument('--window-size=1600,900')
    driver = webdriver.Chrome(chrome_options=options)
    web_app_setup.navigate_to_main_page()
    # Users and Pages defined
    first_name = 'Account' + gen_rand_value.random_string(5)
    last_name = 'CreationTest' + gen_rand_value.random_string(5)
    email = first_name.replace(' ', '_') + '@' + last_name.replace(' ', '_') + '.org'
    password = 'testpw' + gen_rand_value.random_number(2)
    create_account = page_utility.AccountCreationPage(driver)
    address = gen_rand_value.random_number(3) + ' West ' + gen_rand_value.random_string(6) + ' Circle'
    city = gen_rand_value.random_string(3)
    state = 'Utah'
    zipcode = gen_rand_value.random_number(5)
    country = 'United States'
    mobile = gen_rand_value.random_number(3) + '-' + gen_rand_value.random_number(
        3) + '-' + gen_rand_value.random_number(4)
    try:
        # Navigate to account creation page
        create_account.navigate_to_account_creation()
        create_account.wait_for_load_complete()
        # Fill out initial email
        create_account.enter_new_account_email(email)
        # Fill out form
        create_account.enter_first_name(first_name)
        create_account.enter_last_name(last_name)
        create_account.enter_password(password)
        create_account.enter_address(address)
        create_account.enter_city(city)
        create_account.enter_state(state)
        create_account.enter_zipcode(zipcode)
        create_account.enter_country(country)
        create_account.enter_mobile_phone(mobile)
        # Submit form
        create_account.click_register()
        # Attempt Login


    except (Exception, BaseException) as e:
        print('Exception occurred: {}'.format(e), True)
    finally:
        driver.quit()
