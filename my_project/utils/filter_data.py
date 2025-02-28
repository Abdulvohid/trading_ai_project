import pandas as pd
from utils.database import get_all_data, save_data

def filter_data():
    """ AI uchun ma'lumotlarni filtrlaymiz """
    data = get_all_data("historical_data")

    if not data:
        print("⚠️ Bazada `historical_data` yo‘q!")
        return

    df = pd.DataFrame(data)

    # ✅ **NaN timeframe'larni to'g'ri timeframe bilan almashtiramiz**
    df["timeframe"].fillna("D1", inplace=True)

    # **Tayyorlangan ma'lumotlarni bazaga saqlash**
    cleaned_data = df.to_dict("records")
    save_data("historical_data_cleaned", cleaned_data)

    print(f"✅ Tozalangan ma'lumotlar: {len(cleaned_data)} ta saqlandi!")

if __name__ == "__main__":
    filter_data()