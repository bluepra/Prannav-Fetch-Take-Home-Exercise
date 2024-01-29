from process_receipts import calculate_reward_points
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
    test_passed = True

    # Test the target receipt
    expected_pts = 31
    actual_pts = calculate_reward_points(target_receipt)

    if expected_pts != actual_pts:
        test_passed = False

    return test_passed

def test_target2_receipt() -> bool:
    test_passed = True

    # Test the target2 receipt
    expected_pts = 28
    actual_pts = calculate_reward_points(target2_receipt)

    if expected_pts != actual_pts:
        test_passed = False

    return test_passed

def test_corner_market_receipt() -> bool:
    test_passed = True

    # Test the corner market receipt
    expected_pts = 109
    actual_pts = calculate_reward_points(corner_market_receipt)

    if expected_pts != actual_pts:
        test_passed = False

    return test_passed

def test_walgreens_receipt() -> bool:
    test_passed = True

    # Test the corner market receipt
    expected_pts = 15
    actual_pts = calculate_reward_points(walgreens_receipt)

    if expected_pts != actual_pts:
        test_passed = False

    return test_passed


if __name__ == '__main__':
    print('Result of test_target_receipt is', test_target_receipt())
    print('Result of test_target2_receipt is', test_target2_receipt())
    print('Result of test_corner_market_receipt is', test_corner_market_receipt())
    print('Result of test_walgreens_receipt is', test_walgreens_receipt())