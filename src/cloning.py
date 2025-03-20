import json
import random
import time
import copy

class Cloner:
    def __init__(self):
        """ذخیره اطلاعات کلون‌ها و الگوها"""
        self.clones = {}

    def create_clone(self, user_data):
        """ایجاد یک کلون از داده‌های کاربر"""
        clone_id = f"clone_{random.randint(1000, 9999)}"
        self.clones[clone_id] = copy.deepcopy(user_data)
        print(f"✅ کلون جدید ساخته شد: {clone_id}")
        return clone_id

    def simulate_behavior(self, clone_id):
        """شبیه‌سازی رفتار کلون‌شده"""
        if clone_id not in self.clones:
            print("⛔ کلون پیدا نشد!")
            return
        
        clone_data = self.clones[clone_id]
        print(f"🤖 شبیه‌سازی رفتار کلون: {clone_data['username']}")

        actions = ["ارسال پیام", "لایک کردن", "پاسخ دادن", "ری‌اکشن", "سکوت کردن"]
        for _ in range(5):
            action = random.choice(actions)
            print(f"📲 {clone_data['username']} الان داره: {action}")
            time.sleep(random.uniform(1, 3))
        
        print("✅ شبیه‌سازی تموم شد!")

    def export_clone(self, clone_id, filename="clone_data.json"):
        """ذخیره اطلاعات کلون در فایل JSON"""
        if clone_id not in self.clones:
            print("⛔ کلون پیدا نشد!")
            return
        
        with open(filename, "w") as file:
            json.dump(self.clones[clone_id], file, indent=4)
        
        print(f"💾 کلون ذخیره شد توی: {filename}")

    def import_clone(self, filename):
        """بارگذاری اطلاعات کلون از فایل JSON"""
        try:
            with open(filename, "r") as file:
                clone_data = json.load(file)
                clone_id = self.create_clone(clone_data)
                print(f"✅ کلون از فایل بارگذاری شد: {clone_id}")
                return clone_id
        except FileNotFoundError:
            print("⛔ فایل پیدا نشد!")
            return None

# --- تست قابلیت کلون ---
if __name__ == "__main__":
    cloner = Cloner()

    # اطلاعات فرضی کاربر
    user_data = {
        "username": "RubikaMaster",
        "status": "online",
        "favorite_actions": ["ارسال پیام", "لایک کردن", "پاسخ دادن"]
    }

    # ساخت کلون
    clone_id = cloner.create_clone(user_data)

    # شبیه‌سازی رفتار کلون
    cloner.simulate_behavior(clone_id)

    # ذخیره کلون به فایل
    cloner.export_clone(clone_id)

    # بازیابی کلون از فایل
    loaded_clone = cloner.import_clone("clone_data.json")
    if loaded_clone:
        cloner.simulate_behavior(loaded_clone
