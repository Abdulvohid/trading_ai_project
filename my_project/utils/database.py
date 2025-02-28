from pymongo import MongoClient

# **MongoDB-ga ulanish**
client = MongoClient("mongodb://localhost:27017/")

# **Database va collectionlarni yaratish**
db = client["ai_trading"]

# 🔹 **Ma'lumot qo‘shish funksiyasi**
def save_data(collection_name, data):
    """MongoDB ga ma'lumot qo‘shish"""
    collection = db[collection_name]
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)
    print(f"✅ `{collection_name}` ga ma'lumot qo‘shildi!")

# 🔹 **Barcha ma'lumotlarni olish funksiyasi**
def get_all_data(collection_name):
    """Barcha ma'lumotlarni olish"""
    collection = db[collection_name]
    data = list(collection.find({}, {"_id": 0}))  # `_id` ni chiqarib tashlaymiz
    print(f"📌 `{collection_name}` dan {len(data)} ta ma'lumot olindi.")
    return data

# 🔹 **Kolleksiyadagi ma'lumotlarni tozalash (FAQAT TEST UCHUN)**
def clear_collection(collection_name):
    """Berilgan kolleksiyadagi barcha ma'lumotlarni o‘chirish"""
    collection = db[collection_name]
    collection.delete_many({})
    print(f"⚠️ `{collection_name}` kolleksiyasi tozalandi!")

# 🔹 **Test qilish**
if __name__ == "__main__":
    test_data = {"symbol": "XAUUSD", "price": 2035.50, "timestamp": "2025-02-28T12:00:00Z"}
    save_data("historical_data", test_data)
    
    all_data = get_all_data("historical_data")
    print("📌 Bazadagi ma'lumotlar:", all_data)
    
    # **Kolleksiyani tozalashni test qilish**
    # clear_collection("historical_data")  # ⚠️ Faqat test uchun, ehtiyot bo‘ling!