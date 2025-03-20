from flask import Flask, render_template, redirect, url_for, request, flash, session
import os
from datetime import datetime

# 🎯 تنظیمات اولیه
app = Flask(__name__)
app.secret_key = "super_secret_key"

# 🔒 کد قفل امنیتی
LOCK_CODE = "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"

# 📍 صفحه قفل امنیتی
@app.route("/", methods=["GET", "POST"])
def lockscreen():
    if request.method == "POST":
        entered_code = request.form.get("password")
        if entered_code == LOCK_CODE:
            session["authenticated"] = True
            flash("✅ دسترسی موفقیت‌آمیز!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("❌ کد اشتباه است!", "error")
            return redirect(url_for("lockscreen"))

    return render_template("lockscreen.html")


# 📊 داشبورد مدیریت
@app.route("/dashboard")
def dashboard():
    if not session.get("authenticated"):
        return redirect(url_for("lockscreen"))
    return render_template("dashboard.html")


# 🔥 نمایش لاگ‌ها
@app.route("/logs")
def logs():
    if not session.get("authenticated"):
        return redirect(url_for("lockscreen"))
    try:
        with open("data/logs/app_log.log", "r") as file:
            logs_content = file.readlines()
        return render_template("logs.html", logs=logs_content[-50:])
    except FileNotFoundError:
        return "🚨 فایل لاگ پیدا نشد!", 404


# 🚀 اجرای سرور
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True
