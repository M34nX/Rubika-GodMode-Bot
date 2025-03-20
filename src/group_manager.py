import requests
from config import BOT_TOKEN

class RubikaGroupManager:
    def __init__(self, bot_token):
        self.token = bot_token
        self.base_url = "https://messenger.rubika.ir/api/"
    
    def create_group(self, group_name, users):
        """📌 ساخت گروه جدید با اعضای مشخص‌شده"""
        payload = {
            "api_version": "5",
            "method": "create_group",
            "input": {
                "token": self.token,
                "name": group_name,
                "members": users
            }
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            print(f"✅ گروه '{group_name}' با موفقیت ساخته شد!")
            return data["data"]["group_guid"]
        else:
            raise Exception(data.get("error", "ساخت گروه ناموفق بود"))

    def add_member(self, group_guid, user_guid):
        """➕ اضافه کردن کاربر جدید به گروه"""
        payload = {
            "api_version": "5",
            "method": "add_group_member",
            "input": {
                "token": self.token,
                "group_guid": group_guid,
                "user_guid": user_guid
            }
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            print(f"✅ کاربر با موفقیت به گروه اضافه شد!")
        else:
            raise Exception(data.get("error", "افزودن کاربر ناموفق بود"))

    def remove_member(self, group_guid, user_guid):
        """❌ اخراج کردن کاربر از گروه"""
        payload = {
            "api_version": "5",
            "method": "remove_group_member",
            "input": {
                "token": self.token,
                "group_guid": group_guid,
                "user_guid": user_guid
            }
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            print("✅ کاربر با موفقیت از گروه حذف شد!")
        else:
            raise Exception(data.get("error", "اخراج کاربر ناموفق بود"))

    def set_admin(self, group_guid, user_guid):
        """👑 دادن مقام ادمین به کاربر"""
        payload = {
            "api_version": "5",
            "method": "set_group_admin",
            "input": {
                "token": self.token,
                "group_guid": group_guid,
                "user_guid": user_guid,
                "admin": True
            }
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            print("✅ کاربر با موفقیت ادمین شد!")
        else:
            raise Exception(data.get("error", "دادن مقام ادمین ناموفق بود"))

    def pin_message(self, group_guid, message_id):
        """📌 پین کردن پیام در گروه"""
        payload = {
            "api_version": "5",
            "method": "pin_message",
            "input": {
                "token": self.token,
                "group_guid": group_guid,
                "message_id": message_id
            }
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            print("✅ پیام با موفقیت پین شد!")
        else:
            raise Exception(data.get("error", "پین کردن پیام ناموفق بود"))

    def get_group_info(self, group_guid):
        """🔍 گرفتن اطلاعات کامل گروه"""
        payload = {
            "api_version": "5",
            "method": "get_group_info",
            "input": {
                "token": self.token,
                "group_guid": group_guid
            }
        }
        response = requests.post(self.base_url, json=payload)
        data = response.json()

        if data.get("status") == "OK":
            return data["data"]
        else:
            raise Exception(data.get("error", "دریافت اطلاعات گروه ناموفق بود"))
