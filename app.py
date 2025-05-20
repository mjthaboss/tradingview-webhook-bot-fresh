from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'TradingView Webhook Bot is live!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    return jsonify({'status': 'success', 'message': 'Webhook received!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
