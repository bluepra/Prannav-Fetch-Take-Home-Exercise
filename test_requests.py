import requests
import json

with open('examples/target-receipt.json') as receipt:
    target_receipt = json.load(receipt)

with open('examples/target2-receipt.json') as receipt:
    target2_receipt = json.load(receipt)

with open('examples/walgreens-receipt.json') as receipt:
    walgreens_receipt = json.load(receipt)

with open('examples/corner-market.json') as receipt:
    corner_market_receipt = json.load(receipt)


def test_target_receipt() -> bool:
    """
    This function tests the Target receipt, and checks if both the
    POST and GET endpoints return expected JSON data.

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    # Test the POST endpoint with target receipt
    post_response = requests.post('http://localhost:5000/receipts/process', json=target_receipt)

    if post_response.status_code != 200:
        test_passed = False

    response_data = post_response.json()

    if 'id' not in response_data:
        test_passed = False

    id = response_data['id']

    # Now test if the ID sucessfully gets us the reward points for the target receipt
    get_response = requests.get(f'http://localhost:5000/receipts/{id}/points')

    if get_response.status_code != 200:
        test_passed = False

    response_data = get_response.json()

    if 'points' not in response_data:
        test_passed = False

    if response_data['points'] != 31:
        test_passed = False

    return test_passed

def test_target2_receipt() -> bool:
    """
    This function tests the Target2 receipt, and checks if both the
    POST and GET endpoints return expected JSON data.

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    # Test the POST endpoint with target receipt
    post_response = requests.post('http://localhost:5000/receipts/process', json=target2_receipt)

    if post_response.status_code != 200:
        test_passed = False

    response_data = post_response.json()

    if 'id' not in response_data:
        test_passed = False

    id = response_data['id']

    # Now test if the ID sucessfully gets us the reward points for the target receipt
    get_response = requests.get(f'http://localhost:5000/receipts/{id}/points')

    if get_response.status_code != 200:
        test_passed = False

    response_data = get_response.json()

    if 'points' not in response_data:
        test_passed = False

    if response_data['points'] != 28:
        test_passed = False

    return test_passed

def test_walgreens_receipt() -> bool:
    """
    This function tests the Walgreens receipt, and checks if both the
    POST and GET endpoints return expected JSON data.

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    # Test the POST endpoint with target receipt
    post_response = requests.post('http://localhost:5000/receipts/process', json=walgreens_receipt)

    if post_response.status_code != 200:
        test_passed = False

    response_data = post_response.json()

    if 'id' not in response_data:
        test_passed = False

    id = response_data['id']

    # Now test if the ID sucessfully gets us the reward points for the target receipt
    get_response = requests.get(f'http://localhost:5000/receipts/{id}/points')

    if get_response.status_code != 200:
        test_passed = False

    response_data = get_response.json()

    if 'points' not in response_data:
        test_passed = False

    if response_data['points'] != 15:
        test_passed = False

    return test_passed

def test_corner_market_receipt() -> bool:
    """
    This function tests the Corner market receipt, and checks if both the
    POST and GET endpoints return expected JSON data.

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    # Test the POST endpoint with target receipt
    post_response = requests.post('http://localhost:5000/receipts/process', json=corner_market_receipt)

    if post_response.status_code != 200:
        test_passed = False

    response_data = post_response.json()

    if 'id' not in response_data:
        test_passed = False

    id = response_data['id']

    # Now test if the ID sucessfully gets us the reward points for the target receipt
    get_response = requests.get(f'http://localhost:5000/receipts/{id}/points')

    if get_response.status_code != 200:
        test_passed = False

    response_data = get_response.json()

    if 'points' not in response_data:
        test_passed = False

    if response_data['points'] != 109:
        test_passed = False

    return test_passed

def test_invalid_id() -> bool:
    """
    This function tests an invalid ID for the GET endpoint.
    We should receive a error message with status 404.

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    invalid_id = '47318413'
    get_response = requests.get(f'http://localhost:5000/receipts/{invalid_id}/points')

    if get_response.status_code != 404:
        test_passed = False

    if get_response.text != 'No receipt found for that id':
        test_passed = False

    return test_passed

def test_invalid_receipts() -> bool:
    """
    This function tests a few invalid receipts. 

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    with open('examples/target-receipt.json') as receipt:
        invalid_target_receipt = json.load(receipt)
    
    # Invalid total
    invalid_target_receipt['total'] = '6.4g'

    post_response = requests.post('http://localhost:5000/receipts/process', json=invalid_target_receipt)

    if post_response.status_code != 400:
        test_passed = False

    if post_response.text != 'The receipt is invalid':
        test_passed = False

    # Correct the total, and enter an invalid purchaseTime
    invalid_target_receipt['total'] = '6.49'
    invalid_target_receipt['purchaseTime'] = '13:1g'

    post_response = requests.post('http://localhost:5000/receipts/process', json=invalid_target_receipt)

    if post_response.status_code != 400:
        test_passed = False

    if post_response.text != 'The receipt is invalid':
        test_passed = False

    # Correct the purchaseTime, and enter an empty items list
    invalid_target_receipt['purchaseTime'] = '13:13'
    invalid_target_receipt['items'] = []

    post_response = requests.post('http://localhost:5000/receipts/process', json=invalid_target_receipt)

    if post_response.status_code != 400:
        test_passed = False

    if post_response.text != 'The receipt is invalid':
        test_passed = False

    return test_passed

def test_non_json_post() -> bool:
    """
    This function tests a few invalid receipts. 

    :return: True if the test passes, false otherwise
    """

    test_passed = True

    post_response = requests.post('http://localhost:5000/receipts/process', data='normal_text_data')

    if post_response.status_code != 400:
        test_passed = False

    if post_response.text != 'The receipt is invalid':
        test_passed = False

    return test_passed



if __name__ == '__main__':
    print('---------- RUNNING TEST_REQUESTS.PY ----------')
    print('Result of test_target_receipt is', test_target_receipt())
    print('Result of test_target2_receipt is', test_target2_receipt())
    print('Result of test_corner_market_receipt is', test_corner_market_receipt())
    print('Result of test_walgreens_receipt is', test_walgreens_receipt())

    print()

    print('Result of test_invalid_id', test_invalid_id())
    print('Result of test_invalid_receipts', test_invalid_receipts())
    print('Result of test_non_json_post', test_non_json_post())