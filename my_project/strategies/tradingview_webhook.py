from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    """TradingView'dan signal olish"""
    try:
        data = request.json
        print(f"📢 Yangi signal: {json.dumps(data, indent=2)}")
        return jsonify({"status": "success", "message": "Signal qabul qilindi"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5000)