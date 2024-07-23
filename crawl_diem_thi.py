
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Cấu hình Selenium WebDriver (ví dụ sử dụng Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Chạy chế độ headless (không mở cửa sổ trình duyệt)

def crawl_data(sbd):
    try_count = 0
    max_tries = 3
    while try_count < max_tries:
        driver = webdriver.Chrome(options=options)
        url = f"https://diemthi.vnexpress.net/index/detail/sbd/{sbd}/year/2024"
        driver.get(url)
        
        data = {'SBD': sbd}
        try:
            WebDriverWait(driver, 35).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="o-detail-thisinh__diemthi"]/table/tbody/tr'))
            )
            
            # Lấy dữ liệu từ bảng điểm thi
            table_rows = driver.find_elements(By.XPATH, '//div[@class="o-detail-thisinh__diemthi"]/table/tbody/tr')
            
            for row in table_rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                if len(cells) == 2:
                    mon_thi = cells[0].text.strip()
                    diem = cells[1].text.strip()
                    data[mon_thi] = diem
            
            driver.quit()
            print(f"Dữ liệu crawl được cho SBD {sbd}: {data}")
            return data
        
        except Exception as e:
            print(f"Lỗi khi lấy dữ liệu cho SBD {sbd}: {e}")
            try_count += 1
            driver.quit()
            time.sleep(2)  # Thêm thời gian chờ giữa các lần thử lại
            if try_count >= max_tries:
                data['Error'] = 'Không tìm thấy dữ liệu'
                return data

def save_to_excel(data_list, filename="diem_thi.xlsx"):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Điểm thi"
    
    headers = ["SBD", "Toán", "Ngữ văn", "Ngoại ngữ", "Vật lý", "Hóa học", "Sinh học", "Lịch sử", "Địa lý", "Giáo dục công dân"]  # Thêm các môn khác nếu cần
    sheet.append(headers)
    
    for data in data_list:
        # Kiểm tra và xóa các dòng trống
        if all(data.get(header, '') == '' for header in headers[1:]):  # Bỏ qua SBD trong kiểm tra
            continue
        row = [data.get(header, '') for header in headers]
        sheet.append(row)
    
    workbook.save(filename)
    abs_path = os.path.abspath(filename)
    print(f"Dữ liệu đã được lưu vào file {filename} tại đường dẫn: {abs_path}")

# Crawl dữ liệu cho danh sách số báo danh từ 01000001 đến 01000101
sbd_list = [f"010{str(i).zfill(5)}" for i in range(1, 102)]

# Sử dụng ThreadPoolExecutor để tăng tốc độ crawl
data_list = []
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(crawl_data, sbd) for sbd in sbd_list]
    for future in as_completed(futures):
        data_list.append(future.result())
        # Lưu dữ liệu tạm thời sau mỗi lần crawl
        if len(data_list) % 100 == 0:
            save_to_excel(data_list, "diem_thi_tam_thoi.xlsx")

# Kiểm tra dữ liệu trước khi lưu
print(f"Dữ liệu sẽ được lưu: {data_list}")

# Lưu dữ liệu vào file Excel trong cùng thư mục với file code này
current_directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_directory, "diem_thi.xlsx")
save_to_excel(data_list, filename)
