from strategies.mt5_connector import connect_mt5, get_mt5_data, close_mt5
from strategies.binance_connector import get_binance_data
from strategies.indicator_strategy import indicator_signal
from utils.telegram_notifier import send_telegram_signal

BOT_TOKEN = "SIZNING_TELEGRAM_BOT_TOKEN"
CHAT_ID = "SIZNING_CHAT_ID"

def main():
    print("🚀 Kod ishga tushdi!")

    # 1. MT5 bilan ulanish
    if connect_mt5():
        mt5_data = get_mt5_data("XAUUSD")  # Tilla uchun ma'lumot olish
        close_mt5()

    # 2. Binance dan ma'lumot olish
    binance_data = get_binance_data("BTCUSDT")

    # 3. Strategiya bo‘yicha signal chiqarish
    if mt5_data is not None:
        mt5_signal = indicator_signal(mt5_data, "XAUUSD")
        print("📊 MT5 Signal:", mt5_signal)
        message = f"📢 MT5 Signal: {mt5_signal['signal']} \n📌 Symbol: {mt5_signal['symbol']} \n🔹 Entry: {mt5_signal['entry']} \n🎯 TP: {mt5_signal['tp']} \n🛑 SL: {mt5_signal['sl']}"
        send_telegram_signal(BOT_TOKEN, CHAT_ID, message)

    if binance_data is not None:
        binance_signal = indicator_signal(binance_data, "BTCUSDT")
        print("📊 Binance Signal:", binance_signal)
        message = f"📢 Binance Signal: {binance_signal['signal']} \n📌 Symbol: {binance_signal['symbol']} \n🔹 Entry: {binance_signal['entry']} \n🎯 TP: {binance_signal['tp']} \n🛑 SL: {binance_signal['sl']}"
        send_telegram_signal(BOT_TOKEN, CHAT_ID, message)

if __name__ == "__main__":
    main()