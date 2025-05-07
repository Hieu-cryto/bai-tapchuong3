import schedule
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# === Cấu hình thông tin email ===
EMAIL_GUI = "hieu_2251220073@dau.edu.vn"
MAT_KHAU_EMAIL = "045204005468"  # App password, không phải mật khẩu Gmail thường
EMAIL_NGUOI_NHAN = "vominhthien100504@gmail.com"

def gui_email_bao_cao():
    # Nội dung email
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = MIMEText(f"📊 m ăn cứt tao À\nThời gian: {now}", "plain", "utf-8")
    message["Subject"] = "🕒 Báo cáo tự động"
    message["From"] = EMAIL_GUI
    message["To"] = EMAIL_NGUOI_NHAN

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_GUI, MAT_KHAU_EMAIL)
            server.send_message(message)
        print(f"[{now}] ✅ Đã gửi email báo cáo.")
    except Exception as e:
        print(f"[{now}] ❌ Lỗi gửi email: {e}")

# === Lên lịch gửi vào 8h sáng và 16h40 chiều ===
schedule.every().day.at("08:00").do(gui_email_bao_cao)
schedule.every().day.at("14:36").do(gui_email_bao_cao)

print("⏳ Đang chạy chương trình gửi email định kỳ...")
while True:
    schedule.run_pending()
    time.sleep(60)