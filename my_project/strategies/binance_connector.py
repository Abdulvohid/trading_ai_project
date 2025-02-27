import requests

BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

def get_binance_price(symbol):
    """Binance API orqali kripto narxlarini olish"""
    try:
        response = requests.get(f"{BINANCE_API_URL}?symbol={symbol}")
        data = response.json()
        return float(data["price"])
    except Exception as e:
        print(f"Binance API xatosi: {e}")
        return None