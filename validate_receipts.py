import re

# This module contains code for validate a receipt, before we process it
# I have written this code, but chosen not to use it since one of the patterns 
# provided is failing to match M&M Corner Market which is a valid retailer name


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


