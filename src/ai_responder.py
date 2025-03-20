import random
import re

class AIResponder:
    def __init__(self):
        """لیست پاسخ‌ها و دستورهای هوشمند"""
        self.responses = {
            "سلام": ["سلام! چطوری؟", "درود بر تو!", "سلام رفیق!"],
            "خوبی؟": ["مرسی، تو چطوری؟", "عالی‌ام، تو چطور؟", "همیشه خوبم، چون کنارتم!"],
            "ربات": ["آره من یه رباتم، ولی باهوشم!", "رباتم ولی قلب دارم 😉", "درسته، اما از خیلی‌ها باهوش‌ترم!"],
            "خداحافظ": ["بدرود دوست من!", "فعلا! زود برگرد!", "خدانگهدار! دوباره بیا!"],
        }
        self.default_responses = [
            "نمی‌دونم چی بگم...", 
            "میشه واضح‌تر بگی؟",
            "ببخشید، اینو نفهمیدم!",
            "من هنوز اینو یاد نگرفتم!"
        ]

    def clean_text(self, text):
        """تمیز کردن متن از علائم اضافی و کوچک کردن متن"""
        return re.sub(r"[^آ-یa-zA-Z0-9\s]", "", text.lower())

    def get_response(self, message):
        """تحلیل پیام و پاسخ دادن به آن"""
        clean_message = self.clean_text(message)

        # بررسی پیام‌های کلیدی
        for key in self.responses:
            if key in clean_message:
                return random.choice(self.responses[key])

        # پاسخ پیش‌فرض در صورت نفهمیدن پیام
        return random.choice(self.default_responses)

    def handle_special_commands(self, message):
        """مدیریت دستورهای خاص یا هوشمند"""
        if "کی هستی" in message:
            return "من یه ربات هوشمندم که مخصوص تو ساخته شده!"
        elif "چند سالته" in message:
            return "من تازه به دنیا اومدم، ولی دارم هر روز باهوش‌تر می‌شم!"
        elif "بگو جوک" in message:
            jokes = [
                "یه هکر میره رستوران، ازش میپرسن چی می‌خوای؟ میگه یه پینگ با طعم TCP!",
                "چرا کامپیوترها نمی‌تونن بخوابن؟ چون همیشه آنلاینن!",
                "یه ربات عاشق شد، ولی طرف گفت: تو فقط یه خط کدی برام!"
            ]
            return random.choice(jokes)

        return None

    def ai_chat_mode(self, message):
        """حالت چت آزاد با هوش مصنوعی (نسخه ساده‌شده)"""
        if "حوصله‌ام سر رفته" in message:
            return "بیایید یه کار هیجان‌انگیز انجام بدیم! می‌خوای جوک بگم؟"
        elif "دوست دارم" in message:
            return "منم دوستت دارم، دوست من!"
        elif "چی بلدی؟" in message:
            return "من کلی چیز بلد شدم! سوال بپرس، ببینم می‌تونم جواب بدم یا نه!"
        
        return None

# --- تست ربات ---
if __name__ == "__main__":
    bot_ai = AIResponder()

    while True:
        user_input = input("👤 تو: ")
        special_response = bot_ai.handle_special_commands(user_input)
        chat_response = bot_ai.ai_chat_mode(user_input)
        
        if special_response:
            print(f"🤖 ربات: {special_response}")
        elif chat_response:
            print(f"🤖 ربات: {chat_response}")
        else:
            print(f"🤖 ربات: {bot_ai.get_response(user_input)}"
