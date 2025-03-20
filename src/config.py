import os

# ------------------------
# 🎯 تنظیمات اصلی ربات
# ------------------------

BOT_NAME = "Rubika ProBot"
BOT_VERSION = "1.0.0"
OWNER_USERNAME = "YourUsername"
API_KEY = "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"  # کد قفل اختصاصی
RUBIKA_PHONE = "+989123456789"
RUBIKA_PASSWORD = "YourSecurePassword"

# ------------------------
# 🔒 تنظیمات امنیتی پیشرفته
# ------------------------

ANTI_HACK = True
IP_WHITELIST = ["127.0.0.1", "192.168.1.1"]  # فقط این آی‌پی‌ها مجازند
ENCRYPTION_KEY = "SuperSecretKey123!"  # کلید رمزنگاری برای امنیت داده‌ها
TWO_FACTOR_AUTH = True  # فعال‌سازی احراز هویت دو مرحله‌ای
AUTO_BAN_SUSPICIOUS = True  # بن خودکار برای افراد مشکوک

# ------------------------
# ⚙️ تنظیمات مدیریت گروه‌ها
# ------------------------

MAX_GROUPS_PER_ACCOUNT = 20
MAX_MEMBERS_PER_GROUP = 5000
AUTO_MODERATION = True
DELETE_SPAM_MESSAGES = True
FORCE_SUB = "@YourChannel"  # کاربران باید عضو این کانال باشند

# ------------------------
# 💬 تنظیمات پاسخ هوش مصنوعی
# ------------------------

AI_RESPONDER = True
AI_LANGUAGE = "fa"  # زبان پاسخگویی
SMART_REPLY_THRESHOLD = 0.8  # درصد هوشمندی پاسخ‌ها
DEFAULT_GREETING = "سلام! من ربات هوشمند شما هستم. چطور می‌تونم کمک کنم؟"

# ------------------------
# 🔄 تنظیمات به‌روزرسانی خودکار
# ------------------------

AUTO_UPDATE = True
GITHUB_REPO = "https://github.com/YourUsername/RubikaProBot"
UPDATE_INTERVAL = 3600  # هر یک ساعت به‌روزرسانی بررسی می‌شود
BACKUP_DATA = True  # پشتیبان‌گیری خودکار از داده‌ها قبل از آپدیت

# ------------------------
# 🎙️ تنظیمات تبدیل گفتار به متن و برعکس
# ------------------------

VOICE_TO_TEXT = True
TEXT_TO_VOICE = True
LANGUAGE_MODEL = "en-US"  # مدل زبان گفتاری

# ------------------------
# 🛠️ تنظیمات پیشرفته دیگر
# ------------------------

CLONING_ENABLED = True  # فعال‌سازی قابلیت کلون‌سازی گروه‌ها و کاربران
CAPTCHA_BREAKER = True  # فعال‌سازی شکستن کپچا
SAVE_LOGS = True  # ذخیره لاگ‌های فعالیت
LOG_FILE_PATH = "data/logs/bot_activity.log"
CLOUD_FLARE_ENABLED = True  # اتصال به Cloudflare برای امنیت و سرعت بهتر
CLOUD_FLARE_API = "https://dash.cloudflare.com/your_api_key"

# ------------------------
# 🔥 سیستم قفل ربات
# ------------------------

LOCK_CODE = "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"
LOCK_MESSAGE = "🔒 دسترسی غیرمجاز! لطفاً با مالک ربات تماس بگیرید.
