import cv2
import pytesseract
import numpy as np
from PIL import Image
import requests
from io import BytesIO

class CaptchaBreaker:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # مسیر تسراکت (برای لینوکس/ترموکس)

    def load_image_from_url(self, url):
        """دریافت تصویر کپچا از URL"""
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            return img
        except Exception as e:
            print(f"⛔ خطا در بارگیری تصویر: {e}")
            return None

    def preprocess_image(self, img):
        """پیش‌پردازش تصویر برای دقت بالاتر OCR"""
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)  # تبدیل به خاکستری
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]  # باینری کردن
        img = cv2.GaussianBlur(img, (3, 3), 0)  # نویزگیری
        return img

    def solve_captcha(self, img):
        """شکستن کپچا با OCR"""
        try:
            img = self.preprocess_image(img)
            captcha_text = pytesseract.image_to_string(img)
            return captcha_text.strip()
        except Exception as e:
            print(f"⚠️ خطای OCR: {e}")
            return ""

    def break_captcha_from_url(self, url):
        """حل کپچا مستقیماً از لینک تصویر"""
        img = self.load_image_from_url(url)
        if img:
            result = self.solve_captcha(img)
            print(f"✅ کپچا شناسایی شد: {result}")
            return result
        return None


# --- تست سیستم کپچا برکر ---
if __name__ == "__main__":
    breaker = CaptchaBreaker()

    # تست حل کپچا از یک لینک
    captcha_url = "https://example.com/captcha.png"
    captcha_result = breaker.break_captcha_from_url(captcha_url)

    # تست کپچای لوکال (برای فایل‌های ذخیره‌شده)
    local_image = Image.open("sample_captcha.png")
    print("✅ کپچای لوکال:", breaker.solve_captcha(local_image)
