import os
import subprocess
import time

class AutoUpdater:
    def __init__(self, repo_url, branch="main"):
        self.repo_url = repo_url
        self.branch = branch
        self.local_dir = os.path.abspath(os.getcwd())
        self.last_commit = self.get_current_commit()

    def get_current_commit(self):
        """🔍 گرفتن شناسه آخرین کامیت محلی"""
        try:
            return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()
        except Exception as e:
            print(f"⚠️ خطا در دریافت کامیت فعلی: {e}")
            return None

    def fetch_latest_commit(self):
        """🔄 گرفتن آخرین کامیت از گیت‌هاب"""
        try:
            subprocess.run(["git", "fetch"], check=True)
            latest_commit = subprocess.check_output(["git", "rev-parse", f"origin/{self.branch}"]).decode("utf-8").strip()
            return latest_commit
        except Exception as e:
            print(f"⚠️ خطا در گرفتن آخرین آپدیت: {e}")
            return None

    def pull_updates(self):
        """📥 دریافت و اعمال آپدیت‌ها"""
        try:
            print("🔄 در حال دریافت آپدیت‌ها از گیت‌هاب...")
            subprocess.run(["git", "pull", "origin", self.branch], check=True)
            print("✅ آپدیت‌ها با موفقیت اعمال شدند!")
            return True
        except Exception as e:
            print(f"⚠️ خطا در به‌روزرسانی: {e}")
            return False

    def restart_bot(self):
        """♻️ ری‌استارت کردن ربات بعد از آپدیت"""
        print("🔄 ری‌استارت ربات برای اعمال تغییرات...")
        time.sleep(3)
        os.execl(sys.executable, sys.executable, *sys.argv)

    def check_for_updates(self):
        """🔎 بررسی دوره‌ای برای آپدیت‌های جدید"""
        print("🔍 بررسی آپدیت‌های جدید...")
        latest_commit = self.fetch_latest_commit()
        if latest_commit and latest_commit != self.last_commit:
            print("✨ نسخه جدید پیدا شد! در حال آپدیت...")
            if self.pull_updates():
                print("✅ ربات آپدیت شد و در حال ری‌استارت است!")
                self.restart_bot()
        else:
            print("✅ ربات به‌روز است!")

if __name__ == "__main__":
    repo_url = "https://github.com/USERNAME/REPO_NAME.git"  # لینک مخزن گیت‌هاب
    branch = "main"  # می‌تونی "master" یا هر شاخه دیگه‌ای رو هم بذاری
    updater = AutoUpdater(repo_url, branch)

    # هر 10 دقیقه یک بار بررسی می‌کنه
    while True:
        updater.check_for_updates()
        time.sleep(600
