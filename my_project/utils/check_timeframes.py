import pandas as pd
from utils.database import get_all_data

# 📥 **Bazadan ma'lumot olish**
data = get_all_data("historical_data_cleaned")

if not data:
    print("⚠️ Bazada tozalangan ma'lumot yo‘q!")
    exit()

# 🔄 **DataFrame ga o'tkazamiz**
df = pd.DataFrame(data)

# **📅 Timestampni datetime formatga o'tkazamiz**
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# 🔍 **Mavjud timeframe'larni tekshiramiz**
print(f"🕒 Eng eski timestamp: {df['timestamp'].min()}")
print(f"🕒 Eng yangi timestamp: {df['timestamp'].max()}")
print(f"🛠 Mavjud timeframe'lar:\n{df['timeframe'].value_counts()}")