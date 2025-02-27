import MetaTrader5 as mt5
import time

# **MT5 ga ulanish**
if not mt5.initialize():
    print("❌ MT5 ga ulanish amalga oshmadi!")
    mt5.shutdown()
else:
    print("✅ MT5 ga muvaffaqiyatli ulandi!")

def get_current_price(symbol="XAUUSD"):
    """
    MT5 dan joriy narxni olish funksiyasi.
    """
    print(f"🔍 `get_current_price({symbol})` chaqirildi!")  # DEBUG

    tick = mt5.symbol_info_tick(symbol)
    if tick:
        print(f"✅ `{symbol}` narxi: {tick.bid} / {tick.ask}")  # DEBUG
        return tick.bid, tick.ask  # Bid va Ask narxlarini qaytarish
    else:
        print(f"❌ `{symbol}` narxlarini olishning imkoni bo'lmadi!")
        return None

# **Test rejimi**
if __name__ == "__main__":
    symbol = "XAUUSD"
    try:
        while True:
            price = get_current_price(symbol)
            time.sleep(1)  # Har 1 soniyada yangilaydi
    except KeyboardInterrupt:
        print("⏹ To‘xtatildi!")

    mt5.shutdown()