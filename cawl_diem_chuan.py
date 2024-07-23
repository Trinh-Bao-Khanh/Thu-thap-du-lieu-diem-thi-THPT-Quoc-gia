from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Danh sách các URL và tên ngành của các ngành cần thu thập
nganh_data = [
    {
        "url": 'https://diemthi.vnexpress.net/tra-cuu-dai-hoc/nganh/id/1644/cid/349',
        "ten_nganh": 'Kỹ thuật Y sinh'
    },{"url": 'https://diemthi.vnexpress.net/tra-cuu-dai-hoc/nganh/id/1633/cid/349',
        "ten_nganh": 'Tự động hóa và Hệ thống điện'
        },{"url": 'https://diemthi.vnexpress.net/tra-cuu-dai-hoc/nganh/id/1643/cid/349',
        "ten_nganh": 'Điện tử - Viễn thông'}
    # Thêm các URL và tên ngành khác ở đây
]

# Tạo danh sách để lưu trữ tất cả dữ liệu
data = []

# Cấu hình Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Chạy Chrome ở chế độ headless
chrome_options.add_argument("--disable-gpu")  # Tắt GPU (cải thiện hiệu năng)
chrome_options.add_argument("--no-sandbox")  # Bỏ qua sandbox (yêu cầu nếu chạy trong container)
chrome_options.add_argument("--ignore-certificate-errors")  # Bỏ qua lỗi SSL
service = Service(ChromeDriverManager().install())

# Hàm để crawl dữ liệu từ một URL và tên ngành
def crawl_data(url, ten_nganh):
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    time.sleep(30)  # Chờ trang web tải xong

    # Lấy các phần tử chứa dữ liệu từ biểu đồ Highcharts
    labels = driver.find_elements(By.CSS_SELECTOR, '.highcharts-data-labels g text tspan:last-of-type')

    # Tạo danh sách để lưu trữ dữ liệu
    years = [2017, 2018, 2019, 2020, 2021, 2023]

    # Kiểm tra xem có nhãn dữ liệu hay không
    if labels:
        for i, label in enumerate(labels):
            score = label.text.strip()
            if i < len(years):  # Đảm bảo không vượt quá số năm đã định
                data.append({
                    "Năm": years[i],
                    "Điểm chuẩn": score,
                    "Ngành": ten_nganh  # Thêm tên ngành
                })

    driver.quit()  # Đóng trình duyệt sau khi thu thập dữ liệu

# Lặp qua từng ngành để thu thập dữ liệu
for nganh in nganh_data:
    crawl_data(nganh["url"], nganh["ten_nganh"])

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Lưu DataFrame vào file Excel
duong_dan_excel = "DiemChuan_NhieuNganh.xlsx"
df.to_excel(duong_dan_excel, index=False)

print(f"Dữ liệu đã được ghi vào {duong_dan_excel}")
