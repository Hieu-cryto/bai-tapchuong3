# BDS Dothi Scraper

## Giới thiệu

Đây là một script Python sử dụng Selenium để tự động thu thập dữ liệu các tin đăng **bán nhà riêng tại Đà Nẵng** trên website [dothi.net](https://dothi.net/). Chương trình sẽ tự động thao tác trên trình duyệt, chọn đúng loại bất động sản và tỉnh thành, sau đó duyệt qua từng trang kết quả, lấy thông tin chi tiết từng bài đăng và lưu lại vào file Excel.

## Tính năng

- **Tự động chọn loại bất động sản**: Script sẽ chọn mục "Bán nhà riêng" trên trang chủ.
- **Tự động chọn tỉnh thành**: Script chọn "Đà Nẵng" trong danh sách tỉnh/thành phố.
- **Duyệt qua nhiều trang**: Tự động chuyển trang để lấy toàn bộ dữ liệu.
- **Thu thập thông tin chi tiết**: Lấy tiêu đề, mô tả, giá, diện tích, địa chỉ, link bài đăng.
- **Xuất dữ liệu ra Excel**: Dữ liệu được lưu vào file `BDSDothi.xlsx`.
- **Tự động chạy theo lịch**: Sử dụng thư viện `schedule` để chạy tự động vào 6h sáng mỗi ngày.

## Yêu cầu

- Python 3.7 trở lên
- Google Chrome và ChromeDriver tương thích
- Các thư viện: `selenium`, `pandas`, `schedule`

Cài đặt thư viện:
```bash
pip install selenium pandas schedule
```

Tải [ChromeDriver](https://chromedriver.chromium.org/downloads) phù hợp với phiên bản Chrome bạn đang dùng và đặt vào thư mục chứa script hoặc thêm vào PATH.

## Hướng dẫn sử dụng

1. **Chạy script**
   - Mở terminal/cmd tại thư mục chứa file `bds_hieu.py`
   - Thực thi:
     ```bash
     python bds_hieu.py
     ```
   - Trình duyệt sẽ tự động mở, thao tác chọn loại bất động sản và tỉnh thành, sau đó bắt đầu thu thập dữ liệu.

2. **Kết quả**
   - Dữ liệu sẽ được lưu vào file `BDSDothi.xlsx` trong cùng thư mục với script.
   - File Excel sẽ chứa các cột: Tiêu đề, Mô tả, Giá, Diện tích, Địa chỉ, Link.

3. **Tự động chạy theo lịch**
   - Script sẽ tự động chạy vào 6h sáng mỗi ngày nếu bạn để chương trình chạy liên tục.
   - Để dừng chương trình, nhấn `Ctrl+C` trong terminal.

## Lưu ý

- Script sử dụng Selenium nên sẽ mở trình duyệt Chrome khi chạy.
- Nếu giao diện website thay đổi, bạn cần cập nhật lại các selector trong code.
- Đảm bảo kết nối internet ổn định khi chạy script.
- Script chỉ phục vụ mục đích học tập, nghiên cứu dữ liệu bất động sản.



