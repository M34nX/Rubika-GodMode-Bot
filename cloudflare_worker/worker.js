// Cloudflare Worker — همیشه آنلاین برای روبیکا 🚀

addEventListener("fetch", (event) => {
    event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
    const { pathname } = new URL(request.url);

    // 🔐 صفحه قفل امنیتی با رمز شخصی
    if (pathname === "/lock") {
        return new Response(
            `<h1>🔒 Locked</h1><p>رمز اشتباه است یا شما اجازه ورود ندارید!</p>`,
            { status: 403 }
        );
    }

    // 🚀 اتصال دائمی به روبیکا
    if (pathname === "/connect") {
        const rubikaAPI = "https://messenger.rubika.ir/api";
        const rubikaToken = "YOUR_RUBIKA_TOKEN"; // حتماً توکن مخصوص روبیکا رو اینجا بذار!

        try {
            const response = await fetch(`${rubikaAPI}/getUpdates`, {
                headers: { Authorization: `Bearer ${rubikaToken}` },
            });
            const data = await response.json();

            if (data.ok) {
                return new Response(JSON.stringify(data.result), { status: 200 });
            } else {
                return new Response("❌ خطای اتصال به روبیکا!", { status: 500 });
            }
        } catch (error) {
            return new Response(`❌ اتصال ناموفق: ${error.message}`, { status: 500 });
        }
    }

    // ✨ پاسخ به درخواست‌های معمولی
    return new Response("🌟 Cloudflare Worker Active!", { status: 200 });
}

// 🛠️ اتصال خودکار به ربات و آپدیت‌ها
setInterval(async () => {
    const pingURL = "https://your-worker-url.cloudflareworkers.com/connect";
    try {
        const pingResponse = await fetch(pingURL);
        console.log("✅ ارتباط با روبیکا برقرار شد:", await pingResponse.text());
    } catch (error) {
        console.error("❌ خطای ارتباط با روبیکا:", error);
    }
}, 60000); // هر دقیقه یکبار درخواست می‌فرست
