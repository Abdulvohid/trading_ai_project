import requests

# Telegram API ma'lumotlari
TELEGRAM_BOT_TOKEN = "8073965773:AAGnEzPaYp6M3PcfmRVK4Vk4pDKUZqyYvTY"
CHAT_ID = "1228701120"

def send_message(message):
    """
    Berilgan matnli xabarni Telegramga yuborish funksiyasi.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    
    print("🛠️ Telegramga yuborish jarayoni boshlandi...")
    print("📩 URL:", url)
    print("📜 Yuborilayotgan xabar:", message)
    
    try:
        response = requests.post(url, data=data)
        print("DEBUG: Telegram javobi:", response.status_code, response.text)
        if response.status_code == 200:
            print("✅ Xabar muvaffaqiyatli yuborildi!")
        else:
            print(f"❌ Xatolik: {response.text}")
    except Exception as e:
        print(f"🚨 Xatolik yuz berdi: {e}")

# Agar fayl to‘g‘ridan-to‘g‘ri chaqirilsa, test xabari yuborish
if __name__ == "__main__":
    send_message("🔔 Test xabari: Telegram bot ishlayapti!")