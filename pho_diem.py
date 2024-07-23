import matplotlib.pyplot as plt
import pandas as pd

# Đọc file Excel
file_path = 'diem_thi.xlsx'
data = pd.read_excel(file_path)

# Lấy danh sách các môn thi từ cột, bỏ cột SBD và cột "Số môn thi"
subjects = data.columns[1:]

# Vẽ biểu đồ cột cho từng môn thi
for subject in subjects:
    plt.figure(figsize=(10, 6))
    
    # Lấy dữ liệu điểm cho môn hiện tại, bỏ qua các giá trị bị trống
    subject_scores = data[subject].dropna()
    
    # Vẽ biểu đồ cột cho môn hiện tại
    plt.hist(subject_scores, bins=10, edgecolor='black', color='skyblue')
    plt.xlabel('Điểm thi')
    plt.ylabel('Số lượng thí sinh')
    plt.title(f'Phổ điểm thi môn {subject}')
    plt.grid(axis='y')

    # Lưu biểu đồ cột thành ảnh
    # bar_chart_path = f'{subject}_pho_diem.png'
    # plt.savefig(bar_chart_path)
    plt.show()