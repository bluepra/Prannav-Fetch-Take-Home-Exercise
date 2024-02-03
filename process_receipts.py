import math


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
    This function tallies up 10 points if the purchase time after 2 PM and before 4 PM

    :param purchase_time: The string format ('hh:mm') of the time of purchase following a 24 hour clock
    :return: Points collected for this rule
    """

    pts = 0

    # Since purchase_time is a string of format hh:mm
    # we have to extract the hour number. Time is given in 24 hour format
    hour = int(purchase_time.split(':')[0])
    mins = int(purchase_time.split(':')[-1])

    if mins > 59:
        raise ValueError('Minutes in purchaseTime are invalid')

    # Allow receipts on or after 14:01 and on or before 15:59
    if (hour == 14 and mins > 0) or hour == 15:
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