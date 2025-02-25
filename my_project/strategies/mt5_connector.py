import MetaTrader5 as mt5
import pandas as pd
import time

def connect_mt5():
    """ MT5 ga ulanadi """
    if not mt5.initialize():
        print("❌ MT5 ga ulanishda xatolik:", mt5.last_error())
        return False
    print("✅ MT5 ga ulanish muvaffaqiyatli!")
    return True

def get_mt5_data(symbol, timeframe=mt5.TIMEFRAME_M1, bars=100):
    """ MT5 dan ohirgi bar ma’lumotlarini olish """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    if rates is None:
        print(f"❌ {symbol} uchun ma’lumot topilmadi.")
        return None

    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def close_mt5():
    """ MT5 bog‘lanishni yopish """
    mt5.shutdown()