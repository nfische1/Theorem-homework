import requests

request_product_url = 'http://automationpractice.com/index.php?rand=1619785489380'
header_def = {'Content-Type': 'text/html', 'Accept': 'application/json'}


def post(url, headers):
    # print('\nWeb Request Sending: {}'.format(json.dumps(json_data)))
    resp = requests.post(url=url, headers=headers)
    # print('Web Response: {}'.format(resp.text))
    return resp


def test_add_item_to_cart(record_xml_attribute):
    record_xml_attribute("name", "Verify selecting an item to put in a cart does not return an error")
    resp = post(request_product_url, header_def)
    assert resp.status_code == 200
