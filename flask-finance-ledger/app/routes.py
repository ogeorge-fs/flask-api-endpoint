from flask import request, jsonify
from app import app, db
from app.models import Account, Transaction

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.get_json()
    account = Account(name=data['name'], type=data['type'])
    db.session.add(account)
    db.session.commit()
    return jsonify({'message': 'Account created', 'id': account.id})

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    account = Account.query.get(data['account_id'])
    if not account:
        return jsonify({'message': 'Account not found'}), 404
    transaction = Transaction(account_id=account.id, amount=data['amount'], type=data['type'])
    if data['type'] == 'debit':
        account.balance += data['amount']
    elif data['type'] == 'credit':
        account.balance -= data['amount']
    else:
        return jsonify({'message': 'Invalid transaction type'}), 400
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction recorded'})

@app.route('/balance/<int:account_id>', methods=['GET'])
def get_balance(account_id):
    account = Account.query.get(account_id)
    if not account:
        return jsonify({'message': 'Account not found'}), 404
    return jsonify({'account': account.name, 'balance': account.balance})

@app.route('/trial-balance', methods=['GET'])
def trial_balance():
    accounts = Account.query.all()
    debits = sum(a.balance for a in accounts if a.type.lower() in ['asset', 'expense'])
    credits = sum(-a.balance for a in accounts if a.type.lower() in ['liability', 'income'])
    balanced = debits == credits
    return jsonify({'debits': debits, 'credits': credits, 'balanced': balanced})
