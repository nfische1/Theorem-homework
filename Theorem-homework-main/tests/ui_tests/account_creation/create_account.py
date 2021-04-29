from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests import web_app_setup, gen_rand_num,page_utility


def test_create_account():
    # Setup Driver, define options
    options = Options()
    # Comment out the line below if you want to see the test run
    options.add_argument('--headless')
    options.add_argument('--window-size=1600,900')
    driver = webdriver.Chrome(chrome_options=options)
    web_app_setup.navigate_to_main_page()
    # Users and Pages defined
    first_name = 'NewFE' + gen_rand_num.random_string(5)
    last_name = 'EmpFE' + gen_rand_num.random_string(5)
    email = first_name.replace(' ', '_') + '@' + last_name.replace(' ', '_') + '.org'
    create_account = page_utility.AccountCreationPage(driver)
    account_creation_page = create_account.account_creation_page()
    try:

    except (Exception, BaseException) as e:
        print('Exception occurred: {}'.format(e), True)
    finally:
        driver.quit()