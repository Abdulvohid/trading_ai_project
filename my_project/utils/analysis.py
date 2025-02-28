from utils.database import get_all_data
import pandas as pd

def analyze_data():
    """Bazadagi ma'lumotlarni yuklab, oddiy statistik tahlil qilish"""
    
    # MongoDB dan ma'lumotlarni olish
    data = get_all_data("historical_data")  # yoki "live_data"
    
    if not data:
        print("⚠️ Bazada ma'lumot yo‘q!")
        return
    
    # Pandas DataFramega o‘tkazish
    df = pd.DataFrame(data)
    
    # Statistik tahlil
    print("📊 Bazadagi ma'lumotlar:")
    print(df.describe())  # Statistika (min, max, o'rtacha va h.k.)
    
    return df

if __name__ == "__main__":
    analyze_data()