import requests

EXNESS_API_URL = "https://trading-api.exness.com/api/v1/prices"

def get_exness_price(symbol, token):
    """Exness API orqali Forex va XAUUSD narxlarini olish"""
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{EXNESS_API_URL}/{symbol}", headers=headers)
        data = response.json()
        return float(data["ask"])  # Asosiy narx
    except Exception as e:
        print(f"Exness API xatosi: {e}")
        return None