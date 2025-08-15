from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# In-memory "database"
accounts = {
    "12345": {"balance": 500},
    "67890": {"balance": 1000}
}

@app.route('/')
def home():
    logging.info("Home endpoint accessed")
    return {"message": "ATM API is running"}

@app.route('/accounts/<account_number>/balance', methods=['GET'])
def get_balance(account_number):
    account = accounts.get(account_number)
    if not account:
        logging.warning(f"Balance check failed: Account {account_number} not found")
        return jsonify({"error": "Account not found"}), 404

    logging.info(f"Balance check: Account {account_number} has {account['balance']}")
    return jsonify({
        "account_number": account_number,
        "balance": account["balance"]
    })

@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw(account_number):
    account = accounts.get(account_number)
    if not account:
        logging.warning(f"Withdraw failed: Account {account_number} not found")
        return jsonify({"error": "Account not found"}), 404

    try:
        data = request.get_json()
        amount = float(data.get("amount", 0))
    except (TypeError, ValueError):
        logging.warning(f"Withdraw failed: Invalid amount input for account {account_number}")
        return jsonify({"error": "Invalid amount"}), 400

    if amount <= 0:
        logging.warning(f"Withdraw failed: Non-positive amount for account {account_number}")
        return jsonify({"error": "Amount must be positive"}), 400
    if account["balance"] < amount:
        logging.warning(f"Withdraw failed: Insufficient funds in account {account_number}")
        return jsonify({"error": "Insufficient funds"}), 400

    account["balance"] -= amount
    logging.info(f"Withdraw successful: {amount} withdrawn from account {account_number}")
    return jsonify({
        "account_number": account_number,
        "new_balance": account["balance"]
    })

@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit(account_number):
    account = accounts.get(account_number)
    if not account:
        logging.warning(f"Deposit failed: Account {account_number} not found")
        return jsonify({"error": "Account not found"}), 404

    try:
        data = request.get_json()
        amount = float(data.get("amount", 0))
    except (TypeError, ValueError):
        logging.warning(f"Deposit failed: Invalid amount input for account {account_number}")
        return jsonify({"error": "Invalid amount"}), 400

    if amount <= 0:
        logging.warning(f"Deposit failed: Non-positive amount for account {account_number}")
        return jsonify({"error": "Amount must be positive"}), 400

    account["balance"] += amount
    logging.info(f"Deposit successful: {amount} deposited to account {account_number}")
    return jsonify({
        "account_number": account_number,
        "new_balance": account["balance"]
    })

if __name__ == '__main__':
    app.run(debug=True)
