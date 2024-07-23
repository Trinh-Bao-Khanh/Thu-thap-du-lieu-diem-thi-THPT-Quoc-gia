
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Đọc dữ liệu từ file Excel
file_path = "DiemChuan_NhieuNganh.xlsx"
df = pd.read_excel(file_path)

# Lọc dữ liệu bị thiếu
df_clean = df.dropna(subset=['Điểm chuẩn'])

# Khởi tạo model dự báo
model = LinearRegression()

# Lưu kết quả dự báo
predictions = []

# Dự báo điểm chuẩn cho từng ngành
for nganh in df['Ngành'].unique():
    df_nganh = df_clean[df_clean['Ngành'] == nganh]
    X = df_nganh[['Năm']]
    y = df_nganh['Điểm chuẩn']
    
    model.fit(X, y)
    # Chuyển đổi giá trị cần dự báo thành DataFrame với tên cột hợp lệ
    prediction = model.predict(pd.DataFrame([[2024]], columns=['Năm']))
    
    predictions.append({'Ngành': nganh, 'Dự báo Điểm chuẩn 2024': prediction[0]})

# Tạo dataframe từ kết quả dự báo
df_predictions = pd.DataFrame(predictions)

# Lưu kết quả dự báo vào file Excel
output_file_path = "DiemChuan_DuBao_2024.xlsx"
df_predictions.to_excel(output_file_path, index=False)

output_file_path
