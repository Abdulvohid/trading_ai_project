import pandas as pd
from utils.database import get_all_data

# 📥 **Bazadan ma'lumot olish**
historical = get_all_data("historical_data")
live = get_all_data("live_data")

# 🛠 **Bazadagi ma'lumotlar sonini chiqarish**
print(f"📊 Tarixiy ma'lumotlar soni: {len(historical)}")
print(f"📊 Joriy ma'lumotlar soni: {len(live)}")

# 📌 **Birinchi 5 ta tarixiy ma'lumot**
if historical:
    df = pd.DataFrame(historical)
    
    print("📌 Birinchi 5 tarixiy ma'lumot:")
    print(df.head(5))

    # 📅 **Timeframe va NaN qiymatlarni tekshiramiz**
    print(f"🕒 Mavjud timeframe'lar: {df['timeframe'].unique()}")
    print(f"❗ NaN qiymatlar: \n{df.isna().sum()}")

# 📌 **Birinchi 5 ta joriy ma'lumot**
if live:
    df_live = pd.DataFrame(live)

    print("📌 Birinchi 5 live ma'lumot:")
    print(df_live.head(5))
    
    print(f"🕒 Joriy timeframe'lar: {df_live['timeframe'].unique()}")
    print(f"❗ NaN qiymatlar: \n{df_live.isna().sum()}")