import pandas as pd
import ta  # pip install ta

def indicator_signal(df, symbol):
    """
    Sodda RSI indikatori asosida signal yaratish:
    RSI < 30 => BUY, RSI > 70 => SELL, aks holda HOLD.
    Qo‘shimcha ma’lumotlar: symbol (instrument) va entry zone.
    """

    # RSI hisoblash
    rsi_indicator = ta.momentum.RSIIndicator(df['Close'], window=14)
    df['rsi'] = rsi_indicator.rsi()

    # Oxirgi RSI va Close qiymati
    last_rsi = df['rsi'].iloc[-1]
    entry_price = df['Close'].iloc[-1]  # Kirish narxi

    # Signal yaratish
    if last_rsi < 30:
        signal = "BUY"
    elif last_rsi > 70:
        signal = "SELL"
    else:
        signal = "HOLD"

    return {
        "symbol": symbol,
        "signal": signal,
        "entry": round(entry_price, 2),  # Entry zone
        "tp": round(entry_price * 1.005, 2),  # TP 0.5% yuqorida
        "sl": round(entry_price * 0.995, 2)   # SL 0.5% pastda
    }