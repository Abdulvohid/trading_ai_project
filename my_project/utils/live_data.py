import sys
import os
import time
from datetime import datetime
from utils.database import save_data
from strategies.mt5_live_price import get_current_price
from strategies.binance_connector import get_binance_price

# **Import yo'lini to'g'ri qilish**
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# **Qidirilayotgan aktivlar**
SYMBOLS_MT5 = ["XAUUSD", "EURUSD"]
SYMBOLS_BINANCE = ["BTCUSDT", "ETHUSDT"]

def collect_live_data():
    while True:
        live_data = []

        # **MT5 narxlarini olish**
        for symbol in SYMBOLS_MT5:
            try:
                price = get_current_price(symbol)
                if price:
                    live_data.append({
                        "symbol": symbol,
                        "price": price,
                        "source": "MT5",
                        "timestamp": datetime.utcnow().isoformat()
                    })
            except Exception as e:
                print(f"❌ {symbol} uchun MT5 narxi olinmadi! Xatolik: {e}")

        # **Binance narxlarini olish**
        for symbol in SYMBOLS_BINANCE:
            try:
                price = get_binance_price(symbol)
                if price:
                    live_data.append({
                        "symbol": symbol,
                        "price": price,
                        "source": "Binance",
                        "timestamp": datetime.utcnow().isoformat()
                    })
            except Exception as e:
                print(f"❌ {symbol} uchun Binance narxi olinmadi! Xatolik: {e}")

        # **Ma'lumotlarni MongoDB'ga saqlash**
        if live_data:
            try:
                save_data("live_data", live_data)
                print(f"✅ {len(live_data)} ta Live ma'lumotlar bazaga qo‘shildi:")
                for entry in live_data:
                    print(entry)
            except Exception as e:
                print(f"❌ Ma'lumotlarni saqlashda xatolik: {e}")
        else:
            print("⚠️ Live ma'lumotlar olinmadi!")

        time.sleep(1)  # **Har 10 soniyada yangi ma'lumot qo‘shish**

if __name__ == "__main__":
    collect_live_data()