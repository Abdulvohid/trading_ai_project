from binance.client import Client
import pandas as pd
import os

# Binance API kalitlari
BINANCE_API_KEY = "SIZNING_BINANCE_API_KEY"
BINANCE_SECRET_KEY = "SIZNING_BINANCE_SECRET_KEY"

client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def get_binance_data(symbol="BTCUSDT", interval=Client.KLINE_INTERVAL_1MINUTE, bars=100):
    """ Binance dan so‘nggi bar ma’lumotlarini olish """
    klines = client.get_klines(symbol=symbol, interval=interval, limit=bars)
    df = pd.DataFrame(klines, columns=['time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'trades', 'taker_base', 'taker_quote', 'ignore'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df['close'] = df['close'].astype(float)
    return df