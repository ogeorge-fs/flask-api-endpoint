# Flask Finance Ledger API

A simple financial ledger REST API built with Flask and SQLite.

## 📌 Features
- Add financial accounts (Asset, Liability, Income, Expense)
- Record debit/credit transactions
- Fetch account balances
- View a trial balance report

## 📚 API Endpoints
| Method | Endpoint            | Description                     |
|:--------|:---------------------|:--------------------------------|
| POST   | /accounts            | Create a new account             |
| POST   | /transactions        | Record a debit or credit         |
| GET    | /balance/<account_id> | Get balance for an account       |
| GET    | /trial-balance        | View total debits and credits    |

## 🚀 Installation
```bash
git clone https://github.com/YOUR_USERNAME/flask-finance-ledger.git
cd flask-finance-ledger
pip install -r requirements.txt
python run.py
