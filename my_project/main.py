from strategies.binance_connector import get_binance_price
from strategies.exness_connector import get_exness_price
import time

TOKEN = "EXNESS_API_TOKEN"  # Exness uchun API token
SYMBOLS = ["BTCUSDT", "ETHUSDT", "XAUUSD", "EURUSD"]

def main():
    while True:
        print("\n📊 Hozirgi narxlar:")
        
        for symbol in SYMBOLS:
            if symbol in ["BTCUSDT", "ETHUSDT"]:
                price = get_binance_price(symbol)
            else:
                price = get_exness_price(symbol, TOKEN)
            
            if price:
                print(f"{symbol}: {price}")
        
        time.sleep(10)  # 10 soniya kutish

if __name__ == "__main__":
    main()