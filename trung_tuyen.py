
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đường dẫn tới các file Excel
file_path_diem_thi = "diem_thi_save1.xlsx"
file_path_diem_chuan_du_bao = "DiemChuan_DuBao_2024.xlsx"

# Đọc dữ liệu điểm thi từ file Excel
df_diem_thi = pd.read_excel(file_path_diem_thi)

# Kiểm tra tên các cột trong file điểm thi
print(df_diem_thi.columns)

# Đọc dữ liệu điểm chuẩn dự báo từ file Excel
df_diem_chuan_du_bao = pd.read_excel(file_path_diem_chuan_du_bao)

# Kiểm tra tên các cột trong file điểm chuẩn dự báo
print(df_diem_chuan_du_bao.columns)

# Lọc các thí sinh có đủ điểm thi cho các môn Toán, Vật lý, Hóa học, Ngoại ngữ
df_diem_thi = df_diem_thi.dropna(subset=['Toán', 'Vật lý', 'Hóa học', 'Ngoại ngữ'])

# Lọc ra các thí sinh có thi tổ hợp A00 và A01
df_A00 = df_diem_thi[['SBD', 'Toán', 'Vật lý', 'Hóa học']].copy()
df_A01 = df_diem_thi[['SBD', 'Toán', 'Vật lý', 'Ngoại ngữ']].copy()

# Tạo danh sách thí sinh đỗ và điểm các môn trúng tuyển
admission_list = []

for index, row in df_diem_chuan_du_bao.iterrows():
    nganh = row['Ngành']
    diem_chuan_2024 = row['Dự báo Điểm chuẩn 2024']
    
    # Xét tổ hợp A00
    df_A00['Tổng điểm A00'] = df_A00['Toán'] + df_A00['Vật lý'] + df_A00['Hóa học']
    df_A00_do = df_A00[df_A00['Tổng điểm A00'] >= diem_chuan_2024]
    
    for _, ts in df_A00_do.iterrows():
        admission_list.append({
            'SBD': ts['SBD'],
            'Ngành': nganh,
            'Tổ hợp': 'A00',
            'Toán': ts['Toán'],
            'Vật lý': ts['Vật lý'],
            'Hóa học': ts['Hóa học'],
            'Tổng điểm': ts['Tổng điểm A00']
        })
    
    # Xét tổ hợp A01
    df_A01['Tổng điểm A01'] = df_A01['Toán'] + df_A01['Vật lý'] + df_A01['Ngoại ngữ']
    df_A01_do = df_A01[df_A01['Tổng điểm A01'] >= diem_chuan_2024]
    
    for _, ts in df_A01_do.iterrows():
        admission_list.append({
            'SBD': ts['SBD'],
            'Ngành': nganh,
            'Tổ hợp': 'A01',
            'Toán': ts['Toán'],
            'Vật lý': ts['Vật lý'],
            'Ngoại ngữ': ts['Ngoại ngữ'],
            'Tổng điểm': ts['Tổng điểm A01']
        })

df_admission = pd.DataFrame(admission_list)

# Vẽ biểu đồ số lượng thí sinh đỗ vào các ngành
plt.figure(figsize=(10, 6))
ax = df_admission.groupby('Ngành').size().plot(kind='bar')
plt.xlabel('Ngành')
plt.ylabel('Số lượng thí sinh đỗ')
plt.title('Số lượng thí sinh đỗ vào các ngành năm 2024')
plt.xticks(rotation=45)
plt.tight_layout()

# Thêm số lượng thí sinh đỗ vào giữa các cột
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height() / 2.),
                ha='center', va='center', fontsize=12, color='white', fontweight='bold')

# plt.savefig("So_luong_thi_sinh_do_2024.png")
plt.show()
# Lưu danh sách thí sinh đỗ và điểm các môn trúng tuyển vào file Excel
output_file_path = "DanhSach_ThiSinh_Do_2024.xlsx"
df_admission.to_excel(output_file_path, index=False)

print(f"Kết quả đã được lưu vào: {output_file_path}")
