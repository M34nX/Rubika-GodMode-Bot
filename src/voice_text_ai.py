import speech_recognition as sr
from gtts import gTTS
import os
import playsound

class VoiceTextAI:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def voice_to_text(self, audio_file=None):
        """تبدیل صدای کاربر به متن"""
        try:
            if audio_file:
                with sr.AudioFile(audio_file) as source:
                    audio_data = self.recognizer.record(source)
            else:
                with sr.Microphone() as source:
                    print("🎙️ درحال گوش دادن...")
                    audio_data = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio_data, language="fa-IR")
            print(f"📝 متن تشخیص داده‌شده: {text}")
            return text

        except sr.UnknownValueError:
            print("⛔ صدای کاربر نامفهوم بود!")
            return ""
        except Exception as e:
            print(f"⚠️ خطا: {e}")
            return ""

    def text_to_voice(self, text, lang="fa"):
        """تبدیل متن به صدای مصنوعی"""
        try:
            tts = gTTS(text=text, lang=lang)
            file_path = "response.mp3"
            tts.save(file_path)
            playsound.playsound(file_path)
            os.remove(file_path)
            print("🔊 پیام صوتی پخش شد!")
        except Exception as e:
            print(f"⚠️ خطای تولید صدا: {e}")

    def auto_reply_voice(self, audio_file=None):
        """گوش میده، متن رو می‌گیره و با هوش مصنوعی جواب می‌ده"""
        user_text = self.voice_to_text(audio_file)
        if user_text:
            response = f"متوجه شدم گفتی: {user_text}!"
            self.text_to_voice(response)


# --- تست هوش مصنوعی صوتی ---
if __name__ == "__main__":
    voice_ai = VoiceTextAI()

    # ۱. تبدیل صدای کاربر به متن
    user_text = voice_ai.voice_to_text()
    
    # ۲. تبدیل متن به صدای مصنوعی
    if user_text:
        voice_ai.text_to_voice("سلام! صدای شما را شنیدم و متن را فهمیدم.")

    # ۳. اجرای حالت خودکار (گوش بده، بفهم، جواب بده)
    voice_ai.auto_reply_voice(
