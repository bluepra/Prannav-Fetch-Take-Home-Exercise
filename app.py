from flask import Flask, request

app = Flask(__name__)

# In memory database for the collected receipts
# Receipt IDs are the keys, and the values are the receipts objects
receipts = {}

@app.route('/')
def home():
    return "Fetch Backend Take Home Exercise - Prannav"

# POST
@app.route('/receipts/process', methods=["POST", "GET"])
def process_receipts():
    if request.method == "POST":
        # Save the request's JSON object as a variable - this is the receipt
        # Generate a random ID for the receipt
        # Add the receipt to the receipts dictionary with the id as the key
        return "Process receipt page - POST accessed"
    else:
        # This might not be needed
        return "Process receipt page - GET accessed"

# GET 
@app.route('/receipts/<id>/points')
def get_points(id):
    # Get the correct receipt from the receipts database using the given id
    # Calculate reward points
    receipt = None
    calculate_reward_points(receipt)
    return f"Getting points for ID {id}"

# This function calculates the correct number of reward points for the given receipt
def calculate_reward_points(receipt):
    pass

if __name__ == '__main__':
    app.run()