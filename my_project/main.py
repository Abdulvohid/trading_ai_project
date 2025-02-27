import sys
import os
import time
from strategies.mt5_live_price import get_current_price  # MT5 narxlarini olish
from strategies.binance_connector import get_binance_price  # Binance narxlarini olish
from utils.telegram_notifier import send_message  # **Yagona funksiyaga o‘tkazildi**

# Import yo‘lini to‘g‘rilash
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Qidirilayotgan aktivlar
SYMBOLS_MT5 = ["XAUUSD", "EURUSD"]
SYMBOLS_BINANCE = ["BTCUSDT", "ETHUSDT"]

def main():
    while True:
        # **Bitta xabarga jamlash**
        message = "📊 Hozirgi narxlar:\n\n"

        # **MT5 narxlarini qo‘shish**
        message += "📈 MT5 Hozirgi narxlar:\n"
        for symbol in SYMBOLS_MT5:
            try:
                price = get_current_price(symbol)
                if price:
                    message += f"{symbol}: {price}\n"
                else:
                    message += f"{symbol}: ❌ Narx olinmadi!\n"
            except Exception as e:
                print(f"❌ `get_current_price({symbol})` ishlamadi: {e}")
                message += f"{symbol}: ❌ Xatolik!\n"

        # **Binance narxlarini qo‘shish**
        message += "\n📉 Binance Hozirgi narxlar:\n"
        for symbol in SYMBOLS_BINANCE:
            try:
                price = get_binance_price(symbol)
                if price:
                    message += f"{symbol}: {price}\n"
                else:
                    message += f"{symbol}: ❌ Binance API ishlamayapti!\n"
            except Exception as e:
                print(f"❌ Binance narxini olishda xatolik: {e}")
                message += f"{symbol}: ❌ Xatolik!\n"

        # **Xabarni terminalga chiqarish va Telegramga yuborish**
        print("🔔 Yuborilayotgan xabar:")
        print(message)

        try:
            send_message(message)  # **Yagona xabar yuborish**
            print("✅ Xabar Telegramga yuborildi!")
        except Exception as e:
            print(f"❌ Telegramga yuborishda xatolik: {e}")

        time.sleep(10)  # **Har 10 soniyada yangilash**

if __name__ == "__main__":
    main()