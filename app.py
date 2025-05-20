from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    # Here, add your trading bot logic to handle the webhook data
    return jsonify({"status": "success", "message": "Webhook received!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
