import os
import time
import threading
from rubika_login import RubikaBot
from group_manager import GroupManager
from ai_responder import AIResponder
from anti_hack import SecuritySystem
from cloning import AccountCloner
from voice_text_ai import VoiceTextAI
from auto_update import AutoUpdater
from captcha_breaker import CaptchaBreaker
from config import BOT_TOKEN, PHONE_NUMBERS, START_MSG

# 🌟 شروع به کار ربات
print("🚀 Rubika GodMode Bot is Starting...")

# ✨ سیستم امنیتی پیشرفته
security = SecuritySystem()
security.verify_access()

# 🔑 ورود به اکانت‌ها و مدیریت گروه‌ها
bot = RubikaBot(BOT_TOKEN, PHONE_NUMBERS)
manager = GroupManager(bot)
ai_responder = AIResponder()
voice_ai = VoiceTextAI()
captcha_breaker = CaptchaBreaker()
cloner = AccountCloner(bot)

# 🔄 سیستم آپدیت خودکار
updater = AutoUpdater()
updater.check_for_update()

# 🌟 خوش‌آمدگویی
print(START_MSG)
bot.send_message("✅ Rubika GodMode Bot is Online!", target="me")

# 🎯 وظایف ربات
def main_loop():
    while True:
        try:
            # 🛡️ بررسی امنیت
            if not security.check_safety():
                print("❗ سیستم به خطر افتاد! ربات خاموش می‌شود.")
                bot.send_message("⚠️ خطر امنیتی شناسایی شد!", target="me")
                break

            # 🔥 مدیریت پیام‌ها
            updates = bot.get_updates()
            for update in updates:
                user_id, message = update["user_id"], update["message"]

                # 🎯 پاسخ هوش مصنوعی به پیام‌ها
                if message.startswith("/"):
                    response = ai_responder.handle_command(message, user_id)
                    bot.send_message(response, user_id)

                # 🔥 تبدیل صوت به متن
                elif message.endswith(".ogg"):
                    text = voice_ai.voice_to_text(bot.download_file(message))
                    bot.send_message(f"🎙️ متن استخراج‌شده: {text}", user_id)

                # 🔒 عبور از کپچا
                elif "captcha" in message.lower():
                    solved = captcha_breaker.solve(message)
                    bot.send_message(f"✅ کپچا حل شد: {solved}", user_id)

                else:
                    bot.send_message("🤖 فرمان نامشخص!", user_id)

            # 🔄 کلون‌سازی شماره‌ها
            if manager.should_clone():
                clone_number = cloner.clone_account()
                bot.send_message(f"🔹 اکانت جدید ساخته شد: {clone_number}", target="me")

            # ⏳ تنظیم فاصله بین چک‌ها
            time.sleep(3)

        except Exception as e:
            bot.send_message(f"⚠️ خطا رخ داد: {e}", target="me")
            time.sleep(5)

# 🚀 اجرای ربات در ترد جدا
threading.Thread(target=main_loop).start()

# 🎯 اجرای پنل مدیریت تحت وب
os.system("python web_panel/app.py"
