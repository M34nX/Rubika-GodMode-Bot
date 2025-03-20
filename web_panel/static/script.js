// --- صفحه قفل امنیتی ---
document.addEventListener("DOMContentLoaded", () => {
    const lockscreen = document.getElementById("lockscreen");
    const dashboard = document.getElementById("dashboard");
    const passwordInput = document.getElementById("password");
    const errorMessage = document.getElementById("error-message");

    const secretPassword = "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";

    document.getElementById("unlock-btn").addEventListener("click", () => {
        if (passwordInput.value === secretPassword) {
            lockscreen.style.display = "none";
            dashboard.style.display = "block";
        } else {
            errorMessage.textContent = "❌ رمز اشتباه است!";
            passwordInput.value = "";
        }
    });

    // فشردن Enter به جای کلیک دکمه
    passwordInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            document.getElementById("unlock-btn").click();
        }
    });
});

// --- بخش نمایش گزارش‌ها به‌صورت زنده ---
const logsContainer = document.getElementById("logs");

function addLog(message) {
    const logEntry = document.createElement("p");
    logEntry.textContent = `🛠️ ${new Date().toLocaleTimeString()} - ${message}`;
    logsContainer.appendChild(logEntry);
    logsContainer.scrollTop = logsContainer.scrollHeight; // اسکرول خودکار به پایین
}

// --- دکمه‌های مدیریتی (مثلاً آپدیت و ریستارت) ---
document.getElementById("update-btn").addEventListener("click", () => {
    addLog("ربات در حال آپدیت است...");
    fetch("/update")
        .then((res) => res.json())
        .then((data) => addLog(data.message))
        .catch((err) => addLog(`❌ خطا در آپدیت: ${err}`));
});

document.getElementById("restart-btn").addEventListener("click", () => {
    addLog("🔄 ربات در حال راه‌اندازی مجدد است...");
    fetch("/restart")
        .then((res) => res.json())
        .then((data) => addLog(data.message))
        .catch((err) => addLog(`❌ خطا در راه‌اندازی مجدد: ${err}`));
});

// --- هشدار ترک صفحه ---
window.onbeforeunload = function () {
    return "آیا مطمئنید می‌خواهید صفحه را ترک کنید؟";
}
