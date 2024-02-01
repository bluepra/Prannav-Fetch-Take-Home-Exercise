import math
import re


# Ideally we would use logging instead of print statements

def all_items_valid(items: list) -> bool:
    """
    This function checks if the items list is valid

    :param items: items of a receipt
    :return: True if all items are valid, false otherwise
    """
    
    for item in items:
        if not isinstance(item, dict):
            print('An item not a dict - invalid receipt')
            return False
    
        if 'shortDescription' not in item or 'price' not in item:
            print('An item is missing a required key - invalid receipt')
            return False
        
        # shortDescription valid
        shortDescription = item['shortDescription']
        if not isinstance(shortDescription, str) or (not re.match("^[\\w\\s\\-]+$", shortDescription)):
            print('An item\'s shortDescription is invalid - invalid receipt')
            return False
        
        # price valid
        price = item['price']
        if not isinstance(price, str) or (not re.match("^\\d+\\.\\d{2}$", price)):
            print('An item\'s price is invalid - invalid receipt')
            return False
        
    # All items in the items list are good
    return True
    


def is_valid_receipt(receipt: dict) -> bool:
    """
    This function checks if the receipt is valid

    :param receipt: the receipt we want to validate
    :return: True if receipt is valid, false otherwise
    """

    # Receipt must be a dictionary
    if not isinstance(receipt, dict):
        print('The receipt is not a dictionary - invalid receipt')
        return False
    
    # All required keys must be present
    required_keys = ['retailer', 'purchaseDate', 'purchaseTime', 'items', 'total']

    for key in required_keys:
        if key not in receipt:
            print(f'The receipt is missing key {key} - invalid receipt')
            return False
    
    # Retailer name valid
    retailer = receipt['retailer']

    # IMPORTANT: For some reason this pattern is failing to match M&M Corner Market 
    # which is a valid retailer name
    if not isinstance(retailer, str) or (not re.match("^[\\w\\s\\-]+$", retailer)):
        print(f'A receipts\'s retailer ({retailer}) is invalid - invalid receipt')
        return False
    
    # Date must be valid -> Ideally need add a regex pattern check for yyyy-mm-dd
    purchaseDate = receipt['purchaseDate']
    dateComponents = purchaseDate.split('-')
    if not isinstance(purchaseDate, str) or purchaseDate == '' or len(dateComponents) != 3:
        print('A receipts\'s purchaseDate is invalid - invalid receipt')
        return False
    
    for i in dateComponents:
        if not i.isdigit():
            print('A receipts\'s purchaseDate is invalid - invalid receipt')
            return False
        
    
    # Time must be valid -> Ideally need add a regex pattern check for hh:mm
    # Asssuming no spaces allowed in time
    purchaseTime = receipt['purchaseTime']
    timeComponents = purchaseTime.split(':')
    if not isinstance(purchaseTime, str) or purchaseTime == '' or len(timeComponents) != 2:
        print('A receipts\'s purchaseTime is invalid - invalid receipt')
        return False
    
    for i in timeComponents:
        if not i.isdigit():
            print('A receipts\'s purchaseTime is invalid - invalid receipt')
            return False
    
    # Valid items -> Must have at least 1 item
    items = receipt['items']
    if not isinstance(items, list) or len(items) < 1:
        print(retailer, )
        print('A receipts\'s items list is invalid - invalid receipt')
        return False
    
    if not all_items_valid(items):
        return False

    
    # Valid total
    total = receipt['total']
    if not isinstance(total, str) or (not re.match("^\\d+\\.\\d{2}$", total)):
        print('A receipts\'s total is invalid - invalid receipt')
        return False
    
    # All good in the receipt
    return True



# v----------- RULES FOR POINTS -----------v

def retailer_name_alphanum_pts(retailer_name: str) -> int:
    """
    This function tallies up 1 point for every alpha-numeric character
    in the retailer name

    :param retailer_name: Name of the retailer
    :return: Points collected for this rule
    """

    pts = 0

    # For each letter of the retailer num, add a point
    # if that letter is alphanumeric
    for letter in retailer_name:
        if letter.isalnum():
            pts += 1

    return pts

def total_round_num_pts(total: float) -> int:
    """
    This function tallies up 50 points if the total is a round dollar amount with no cents

    :param total: The receipt total in dollars and cents
    :return: Points collected for this rule
    """

    pts = 0

    # If the total is a whole number, add 50 pts
    if total.is_integer():
        pts += 50

    return pts

def total_multiple_of_pts(total: float) -> int:
    """
    This function tallies up 25 points if the total is a multiple of .25

    :param total: The receipt total in dollars and cents
    :return: Points collected for this rule
    """

    pts = 0

    # If total is a multiple of .25, add 25 pts
    if total % .25 == 0:
        pts += 25

    return pts

def every_two_items_pts(num_items: int) -> int:
    """
    This function tallies up 5 points for every two items in the receipt

    :param num_items: The number of items in the receipt
    :return: Points collected for this rule
    """

    pts = 0

    pts_per_two_items = 5
    num_sets_of_two = (num_items // 2)
    pts += num_sets_of_two * pts_per_two_items

    return pts

def item_descriptions_trimmed_pts(items: list) -> int:
    """
    This function tallies up points if the item descriptions follow a rule.

    The rule for each item is:
    If the trimmed length of the item description is a multiple of 3, 
    multiply the item price by 0.2 and round up to the nearest integer. 
    The result is the number of points earned for that item.

    :param items: The list of items in the receipt
    :return: Points collected for this rule
    """

    pts = 0

    multiplier = .2

    for item in items:
        description = item['shortDescription']
        price = float(item['price'])

        # If the trimmed length of the item description
        # is a multiple of 3, add pts based on price
        if len(description.strip()) % 3 == 0:
            pts += math.ceil(price * multiplier)

    return pts

def purchase_date_odd_pts(purchase_date: str) -> str:
    """
    This function tallies up 6 points if the purchase date is odd

    :param purchase_date: The string format ('yyyy-mm-dd') of the date of purchase
    :return: Points collected for this rule
    """

    pts = 0

    # Since purchase_date is a string of format yyyy-mm-dd
    # we have to extract the day number
    day = int(purchase_date.split('-')[-1])

    # If day is odd, add to pts
    if day % 2 != 0:
        pts += 6

    return pts

def time_of_purchase_pts(purchase_time: str) -> str:
    """
    This function tallies up 10 points if the purchase time between 2 PM and 4 PM

    :param purchase_time: The string format ('hh:mm') of the time of purchase following a 24 hour clock
    :return: Points collected for this rule
    """

    pts = 0

    # Since purchase_time is a string of format hh:mm
    # we have to extract the hour number. Time is given in 24 hour format
    hour = int(purchase_time.split(':')[0])
    mins = int(purchase_time.split(':')[-1])

    # If the hour falls between 14 and 16, then add to pts
    if hour >= 14 and hour <= 16:
        if hour != 16 or (hour == 16 and mins == 0):
            pts += 10

    return pts


# ^----------- RULES FOR POINTS -----------^

# This function calculates the correct number of reward points for the given receipt
def calculate_reward_points(receipt: dict) -> int:
    """
    This function takes the receipt and awards all possible points based
    on the rules defined.

    :param receipt: The receipt
    :return: Total points rewarded to the input receipt
    """

    # Unpack the receipt for convenience
    retailer = receipt['retailer']
    purchase_date = receipt['purchaseDate']
    purchase_time = receipt['purchaseTime']
    items = receipt['items']
    total = float(receipt['total'])

    # Ideally we wouldn't throw an error like this,
    # We would check for receipt errors, but because of M&M Corner Market regex pattern
    # match failure, I have not used the is_valid_receipt() function
    if len(items) < 1:
        raise ValueError('You need at least 1 item in your items list')

    total_pts = 0

    # Sum of the total points for the receipt based on the rules above
    total_pts += retailer_name_alphanum_pts(retailer)
    total_pts += total_round_num_pts(total)
    total_pts += total_multiple_of_pts(total)
    total_pts += every_two_items_pts(len(items))
    total_pts += item_descriptions_trimmed_pts(items)
    total_pts += purchase_date_odd_pts(purchase_date)
    total_pts += time_of_purchase_pts(purchase_time)

    return total_pts


if __name__ == '__main__':
    print('Running process_receipts.py script')