from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests import web_app_setup


def test_BE7674(environment, record_xml_attribute):
    record_xml_attribute(
        "name",
        "FI-FE-When a user is created, if an admin or treasurer role is selected, their location is auto assigned")
    # Setup Driver, define options
    options = Options()
    # Comment out the line below if you want to see the test run
    options.add_argument('--headless')
    options.add_argument('--window-size=1600,900')
    driver = webdriver.Chrome(chrome_options=options)
    web_app_setup.navigate_to_main_page()
    # Users and Pages defined
    first_name = 'NewFE' + gen_rand_num_id.random_string(5)
    last_name = 'EmpFE' + gen_rand_num_id.random_string(5)
    email = first_name.replace(' ', '_') + '@' + last_name.replace(' ', '_') + '.org'
    employee_page = fi_pages.FiEmployeesPage(driver)
    locator_page = fi_pages.FiEmployeesPageLocators
    try:
        login_page = fi_pages.FiLoginPage(driver)
        login_page.quick_login(bosl_admin)
        employee_page.wait_for_load_complete()
        # Select an employee from the list
        employee_page.click_add_employee()
        employee_page.enter_first_name_field(first_name)
        employee_page.enter_last_name_field(last_name)
        employee_page.enter_email_field(email)
        # Change role to Treasurer
        employee_page.select_employee_role("Treasurer")
        # Verify location is set to treasury
        location = employee_page.new_emp_location_field()
        assert location == 'Treasury'
        assert employee_page.create_emp_button().is_enabled()
        # Change role to admin
        employee_page.select_employee_role("Admin")
        # Verify location is set to technology
        location = employee_page.new_emp_location_field()
        assert location == 'Technology'
        assert employee_page.create_emp_button().is_enabled()
    except (Exception, BaseException) as e:
        print('Exception occurred: {}'.format(e), True)
    finally:
        driver.quit()