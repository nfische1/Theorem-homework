import datetime


def take_screenshot(driver, name=None):
    created_date = str(datetime.datetime.utcnow().strftime("%m-%d-%H%M"))
    add_name = str(name).replace(' ', '')
    file_name = add_name + created_date + '.png'
    driver.save_screenshot('test-reports/screenshots/' + file_name)
