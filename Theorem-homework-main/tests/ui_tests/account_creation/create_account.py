from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests import gen_rand_value, page_utility


def test_create_account():
    # Setup Driver, define options
    options = Options()
    # Comment out the line below if you want to see the test run
    # options.add_argument('--headless')
    options.add_argument('--window-size=1600,900')
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
    # try:
    # Navigate to account creation page
    create_account.navigate_to_account_creation()
    print("Made it to account creation")
    create_account.wait_for_load_complete()
    print("Made it past load complete ")
    # Fill out initial email
    create_account.enter_new_account_email(email)
    print("made it past email entry")
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
    # Login with new account

    # except (Exception, BaseException) as e:
    #     print('Exception occurred: {}'.format(e), True)
    # finally:
    driver.quit()
