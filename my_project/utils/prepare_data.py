import pandas as pd
from utils.database import get_all_data, save_data

def prepare_ai_data():
    """ AI uchun ma'lumotlarni tayyorlash """

    # 📥 **Bazadan ma'lumot olish**
    data = get_all_data("historical_data_cleaned")

    if not data:
        print("⚠️ Bazada ma'lumot yo‘q!")
        return

    # 🔄 **DataFrame ga o'tkazamiz**
    df = pd.DataFrame(data)
    print(f"📊 Boshlang'ich ma'lumotlar soni: {df.shape[0]}")

    # **📅 Timestampni datetime formatga o'tkazamiz**
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)

    # 🔄 **NaN timestamp qatorlarini to'ldirish**
    df["timestamp"] = df["timestamp"].fillna(method="ffill").fillna(method="bfill")

    # **🛑 2020-yildan oldingi ma'lumotlarni o'chiramiz**
    df = df[df["timestamp"] >= pd.Timestamp("2020-01-01", tz="UTC")]

    # ❌ **NaN timeframe'larni o'chiramiz**
    df = df.dropna(subset=["timeframe"])

    # **🔍 Faqat kerakli timeframe’larni qoldiramiz**
    valid_timeframes = ["D1", "H4", "H1", "M15", "M5"]
    df = df[df["timeframe"].isin(valid_timeframes)]

    # 🛑 **NaN `price` qiymatlarni oldini olish**
    df["price"] = df["price"].fillna(method="ffill").fillna(method="bfill")

    # **📈 Narxlarni normalizatsiya qilish**
    price_min, price_max = df["price"].min(), df["price"].max()
    df["normalized_price"] = 1 if price_min == price_max else (df["price"] - price_min) / (price_max - price_min)

    # **🖥️ Muhim loglar**
    print(f"📉 AI uchun tayyor ma'lumotlar soni: {df.shape[0]}")
    print(f"🛠 Mavjud timeframe'lar: {df['timeframe'].unique()}")

    # **AI uchun tayyor ma'lumotlarni saqlash**
    save_data("ai_ready_data", df.to_dict("records"))
    print(f"✅ `ai_ready_data` ga ma'lumot qo‘shildi!")

if __name__ == "__main__":
    prepare_ai_data()