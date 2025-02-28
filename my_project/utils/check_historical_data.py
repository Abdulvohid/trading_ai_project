import pandas as pd
from utils.database import get_all_data

# 📥 **Bazadan `historical_data` ni olish**
data = get_all_data("historical_data")

if not data:
    print("⚠️ `historical_data` bazada yo‘q!")
    exit()

# 🔄 **DataFrame ga o'tkazamiz**
df = pd.DataFrame(data)
print(f"📊 `historical_data` dagi umumiy ma'lumotlar soni: {df.shape[0]}")

# **📅 Timestampni datetime formatga o'tkazamiz**
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)

# 🔍 **Timestamp tekshirish**
print(f"🕒 Eng eski timestamp: {df['timestamp'].min()}")
print(f"🕒 Eng yangi timestamp: {df['timestamp'].max()}")
print(f"⚠️ Timestampdagi NaN qiymatlar soni: {df['timestamp'].isna().sum()}")

# **🔍 Timeframe bo‘yicha statistik ma'lumot**
print(f"📊 Timeframe bo‘yicha statistik ma'lumotlar:\n{df['timeframe'].value_counts()}")

# ❌ **NaN timeframe'larni o'chiramiz**
df = df.dropna(subset=["timeframe"])
print(f"📉 Timeframe bo'sh bo'lgan qatorlar o'chirildi. Yangi soni: {df.shape[0]}")

# **🔍 Faqat kerakli timeframe’larni qoldiramiz**
valid_timeframes = ["D1", "H4", "H1", "M15", "M5"]
df = df[df["timeframe"].isin(valid_timeframes)]
print(f"📉 Kerakli timeframe'lar filtrlashdan keyin: {df.shape[0]}")

# **🛑 NaN `price` qiymatlarni oldini olish**
df["price"] = df["price"].fillna(method="ffill").fillna(method="bfill")

# **📊 Timeframe bo‘yicha qayta tekshirish**
print(f"📊 Timeframe bo‘yicha qayta tekshirish:\n{df['timeframe'].value_counts()}")

# 🖥️ **Test uchun ekranga chiqarish**
print(df.head(20))
print(f"❗ NaN qiymatlar:\n{df.isna().sum()}")