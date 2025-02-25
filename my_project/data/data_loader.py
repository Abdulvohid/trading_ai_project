import os
import pandas as pd

def load_data_csv(filepath):
    """
    CSV faylidan ma'lumot yuklash.
    Kutilgan ustunlar: Date, Open, High, Low, Close, Volume
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Fayl topilmadi: {filepath}")
    df = pd.read_csv(filepath)
    # Sana ustunini datetime'ga aylantirish
    df['Date'] = pd.to_datetime(df['Date'])
    # Sana bo'yicha sortlash
    df.sort_values('Date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def load_data_api(symbol, api_key):
    """
    Misol uchun Alpha Vantage API orqali ma'lumot olish (soddalashtirilgan misol).
    'symbol' = 'XAUUSD' yoki 'BTCUSD' kabi
    """
    # Haqiqiy kod uchun "alpha_vantage" paketi yoki requests bilan GET so'rov
    # Bu yerda soddalashtirilgan muhit:
    # import requests
    # url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=csv"
    # r = requests.get(url)
    # ...
    # DataFrame ga o'girish

    # Hozircha mock data qaytaramiz (bo'sh df)
    df = pd.DataFrame({
        'Date': [],
        'Open': [],
        'High': [],
        'Low': [],
        'Close': [],
        'Volume': []
    })
    return df