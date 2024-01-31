from flask import Flask, request, jsonify
from process_receipts import calculate_reward_points
import uuid

app = Flask(__name__)

# In memory database for the collected receipts
# Receipt IDs are the keys, and the values are the receipts objects
receipts = {}

@app.route('/')
def home():
    return "Fetch Backend Take Home Exercise - Prannav"

# POST
@app.route('/receipts/process', methods=["POST"])
def process_receipts():
    """
    This function serves a POST endpoint which acts to take in a JSON receipt 
    and then save that receipt in an in-memory database.

    :return: A Flask Response Object with the receipt's ID
    """

    try:
        # Save the request's JSON object as a variable - this is the receipt
        receipt = request.get_json()

        # Calculate and save the reward points of the receipt -> Doing this here to avoid 
        # recalculation in the GET request
        receipt['reward_points'] = calculate_reward_points(receipt)

        # Generate a random ID for the receipt
        id = str(uuid.uuid4())

        # Add the receipt to the receipts dictionary with the id as the key
        if id not in receipts:
            receipts[id] = receipt

        return jsonify({'id':id}), 200
    except:
        # If the receipt is invalid, we will end up in this except block
        # So we must return an error message with status code 400
        return 'The receipt is invalid', 400


# GET 
@app.route('/receipts/<id>/points')
def get_points(id):
    """
    This function serves a GET endpoint which acts to provide the client
    with a way to get the number of reward points of a given receipt. 
    The client must provide a receipt id as part of the url

    :return: A Flask Response Object with the receipt's total reward points
    """

    # If the ID is not found, 404 error
    if id not in receipts:
        return 'No receipt found for that id', 404

    # Get the correct receipt from the receipts database using the given id
    receipt = receipts[id]
    
    # Return the reward points
    return jsonify({'points':receipt['reward_points']}), 200


if __name__ == '__main__':
    app.run()