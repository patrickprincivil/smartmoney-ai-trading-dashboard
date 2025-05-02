
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/binance')
def get_binance_balances():
    return jsonify([
        {"asset": "BTC", "total": 0.004872},
        {"asset": "ETH", "total": 0.1057},
        {"asset": "USDT", "total": 255.78}
    ])

@app.route('/api/questrade/account')
def get_questrade_account():
    return jsonify({
        "id": "12345678",
        "type": "Individual",
        "status": "Active"
    })

@app.route('/api/questrade/balances')
def get_questrade_balances():
    return jsonify([
        {"currency": "CAD", "amount": 5123.42},
        {"currency": "USD", "amount": 1287.50}
    ])

@app.route('/api/questrade/positions')
def get_questrade_positions():
    return jsonify([
        {"symbol": "AAPL", "quantity": 15, "avgPrice": 154.32},
        {"symbol": "TSLA", "quantity": 5, "avgPrice": 677.00}
    ])

@app.route('/api/questrade/quote')
def get_questrade_quote():
    symbol = request.args.get("symbol", "AAPL")
    return jsonify({
        "symbol": symbol,
        "last": 178.45,
        "bid": 178.40,
        "ask": 178.50
    })

if __name__ == '__main__':
    app.run(debug=True)
