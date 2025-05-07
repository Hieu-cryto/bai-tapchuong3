import os
import shutil
import smtplib
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Bước 1: Load biến môi trường từ file .env
load_dotenv()

EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')

DATABASE_FOLDER = 'database'
BACKUP_FOLDER = 'backup'

# Bước 2: Hàm gửi email
def send_email(subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Gửi mail thành công: {subject}")
    except Exception as e:
        print(f" Gửi Gmail gặp lỗi: {e}")

# Bước 3: Hàm backup database
def backup_database():
    try:
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)

        backup_count = 0
        for filename in os.listdir(DATABASE_FOLDER):
            if filename.endswith('.sql') or filename.endswith('.sqlite3'):
                source_path = os.path.join(DATABASE_FOLDER, filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_filename = f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}"
                destination_path = os.path.join(BACKUP_FOLDER, backup_filename)

                shutil.copy2(source_path, destination_path)
                backup_count += 1

        if backup_count > 0:
            send_email(
                "Gửi  thành Công",
                f"Đã backup {backup_count} file vào lúc {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
            )
        else:
            send_email(
                " Cảnh báo không tìm thấy thông tintin",
                f"Không tìm thấy file .sql hoặc .sqlite3 để backup lúc {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
            )

    except Exception as e:
        send_email(
            "Gửi thất Bại",
            f"Backup lỗi lúc {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.\nChi tiết lỗi: {e}"
        )

# Bước 4: Hàm chính: hẹn giờ chạy backup
def main():
    schedule.every().day.at("23:32").do(backup_database)
    print(" Đã đặt lịch gửi gmail  vào 23:32 mỗi ngày.")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
