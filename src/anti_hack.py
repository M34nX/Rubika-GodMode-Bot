import hashlib
import requests
import time
from config import BOT_TOKEN

class AntiHack:
    def __init__(self, bot_token):
        self.token = bot_token
        self.base_url = "https://messenger.rubika.ir/api/"
        self.ban_list = set()
        self.protection_level = 3  # 1=کم، 2=متوسط، 3=بیشترین امنیت

    def hash_data(self, data):
        """🔐 هش کردن داده‌ها برای امنیت بیشتر"""
        return hashlib.sha256(data.encode()).hexdigest()

    def detect_spam(self, message, user_guid):
        """⚠️ تشخیص اسپم و لینک‌های خطرناک"""
        spam_keywords = ["http", "www", "free", "promo", "hack", "cheat"]
        if any(keyword in message.lower() for keyword in spam_keywords):
            print(f"⚠️ اسپم شناسایی شد از کاربر: {user_guid}")
            self.ban_user(user_guid)
            return True
        return False

    def ban_user(self, user_guid):
        """🚫 بن کردن کاربر مشکوک به هک یا اسپم"""
        self.ban_list.add(user_guid)
        print(f"🔒 کاربر {user_guid} بن شد و دیگر دسترسی ندارد!")

    def secure_login(self, user_guid):
        """🛡️ قفل دومرحله‌ای برای ورود کاربران مشکوک"""
        challenge_code = self.hash_data(f"{user_guid}{time.time()}")
        print(f"🔐 کد تأیید: {challenge_code[:6]}")
        user_input = input("🔑 کد تایید خود را وارد کنید: ")
        return user_input == challenge_code[:6]

    def check_user_behavior(self, user_guid, message):
        """👁️ مانیتور کردن رفتار مشکوک کاربران"""
        if user_guid in self.ban_list:
            return "⛔️ دسترسی شما محدود شده است!"

        if self.detect_spam(message, user_guid):
            return "🚫 پیام شما به دلیل اسپم حذف شد!"

        # بررسی پیام‌های بیش از حد سریع (حمله اسپم)
        if len(message) > 300 or message.count(" ") < 2:
            self.ban_user(user_guid)
            return "🚫 متن بیش از حد طولانی یا عجیب بود و کاربر مسدود شد!"

        return "✅ پیام امن است!"

    def firewall_protection(self, ip_address):
        """🛡️ محافظت در برابر حملات DDoS و آی‌پی مشکوک"""
        blacklisted_ips = ["192.168.1.1", "203.0.113.42", "45.33.23.12"]
        if ip_address in blacklisted_ips:
            print(f"⚠️ آی‌پی {ip_address} در لیست سیاه است!")
            return False
        print(f"✅ آی‌پی {ip_address} امن است!")
        return True

    def report_attack(self, user_guid, reason):
        """📩 گزارش حمله برای تحلیل بیشتر"""
        payload = {
            "api_version": "5",
            "method": "send_message",
            "input": {
                "token": self.token,
                "object_guid": "admin_guid",
                "message": f"🚨 هشدار امنیتی: کاربر {user_guid} به دلیل '{reason}' مسدود شد!"
            }
        }
        response = requests.post(self.base_url, json=payload)
        if response.json().get("status") == "OK":
            print("✅ گزارش ارسال شد!")
        else:
            print("⚠️ ارسال گزارش ناموفق بود!"
