import MetaTrader5 as mt5
from datetime import datetime
from utils.database import save_data

# **MT5 bilan ulanish**
mt5.initialize()

# **Olish kerak bo'lgan timeframe'lar**
TIMEFRAMES = {
    "D1": mt5.TIMEFRAME_D1,
    "H4": mt5.TIMEFRAME_H4,
    "H1": mt5.TIMEFRAME_H1,
    "M15": mt5.TIMEFRAME_M15,
    "M5": mt5.TIMEFRAME_M5,
}

SYMBOLS = ["XAUUSD", "EURUSD"]

# **Ko'proq ma'lumot olish**
DATA_LIMIT = 10000  # **500 o‘rniga 10,000 ta olamiz**

def fetch_historical_data():
    for symbol in SYMBOLS:
        print(f"📊 `{symbol}` uchun barcha timeframe'lar yuklanmoqda...")
        for tf_name, tf in TIMEFRAMES.items():
            print(f"⏳ `{symbol}` uchun `{tf_name}` ma'lumotlar olinmoqda...")
            
            # **Oxirgi 10,000 ta ma’lumotni yuklab olish**
            rates = mt5.copy_rates_from_pos(symbol, tf, 0, DATA_LIMIT)

            if rates is not None:
                historical_data = []
                for row in rates:
                    historical_data.append({
                        "symbol": symbol,
                        "price": row["close"],  # Yopilish narxi
                        "timestamp": datetime.utcfromtimestamp(row["time"]).isoformat(),
                        "timeframe": tf_name  # **Timeframe qo'shildi**
                    })

                # **Ma'lumotlarni bazaga yozish**
                save_data("historical_data", historical_data)
                print(f"✅ `{symbol}` uchun `{tf_name}` dan {len(historical_data)} ta tarixiy ma'lumot saqlandi!")
            else:
                print(f"❌ `{symbol}` uchun `{tf_name}` ma'lumotlari olinmadi!")

if __name__ == "__main__":
    fetch_historical_data()