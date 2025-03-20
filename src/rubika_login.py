import requests
import json
from config import PHONE_NUMBERS, BOT_TOKEN

class RubikaBot:
    def __init__(self, bot_token, phone_numbers):
        self.token = bot_token
        self.phone_numbers = phone_numbers
        self.sessions = {}
        self.base_url = "https://messenger.rubika.ir/api/"

        print("📲 اتصال به حساب‌ها...")
        self.login_all_accounts()

    def login_all_accounts(self):
        """ورود به همه شماره‌ها و ذخیره سشن‌ها"""
        for phone in self.phone_numbers:
            try:
                print(f"🔹 در حال ورود به: {phone}")
                session = self._start_session(phone)
                self.sessions[phone] = session
                print(f"✅ ورود موفق به {phone}")
            except Exception as e:
                print(f"❗ ورود ناموفق به {phone}: {e}")

    def _start_session(self, phone):
        """ساخت سشن برای یک شماره خاص"""
        payload = {
            "api_version": "5",
            "method": "start_session",
            "input": {"phone": phone, "token": self.token}
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            return data["data"]["session"]
        else:
            raise Exception(data.get("error", "ورود ناموفق"))

    def send_message(self, message, target):
        """ارسال پیام به یوزر یا گروه خاص"""
        for phone, session in self.sessions.items():
            try:
                payload = {
                    "api_version": "5",
                    "method": "send_message",
                    "input": {
                        "session": session,
                        "text": message,
                        "target": target
                    }
                }
                response = requests.post(self.base_url, json=payload)
                if response.json().get("status") != "OK":
                    raise Exception("ارسال پیام ناموفق!")
            except Exception as e:
                print(f"⚠️ خطای ارسال پیام با {phone}: {e}")

    def get_updates(self):
        """گرفتن پیام‌های جدید از روبیکا"""
        updates = []
        for phone, session in self.sessions.items():
            try:
                payload = {
                    "api_version": "5",
                    "method": "get_updates",
                    "input": {"session": session}
                }
                response = requests.post(self.base_url, json=payload)
                data = response.json()
                if data.get("status") == "OK":
                    updates.extend(data["data"]["updates"])
            except Exception as e:
                print(f"⚠️ خطای دریافت پیام‌ها: {e}")

        return updates
