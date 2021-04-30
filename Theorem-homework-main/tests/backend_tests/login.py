import requests


login_url = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
header_def = {'Content-Type': 'text/html', 'Accept': 'application/json'}

def post(url, headers, json):
    # print('\nWeb Request Sending: {}'.format(json.dumps(json_data)))
    resp = requests.post(url=url, headers=headers, json=json)
    # print('Web Response: {}'.format(resp.text))
    return resp


def test_login(record_xml_attribute):
    record_xml_attribute("name", "Verifying login does not return an error")
    resp = post(login_url, header_def, {
        "email": 'email2@email2.com',
        "password": 'password'
    })
    assert resp.status_code == 200