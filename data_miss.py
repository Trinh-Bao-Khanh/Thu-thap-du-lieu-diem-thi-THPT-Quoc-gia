

# import matplotlib.pyplot as plt
# import pandas as pd

# # Đọc file Excel
# file_path = 'diem_thi.xlsx'
# data = pd.read_excel(file_path)

# # Đếm số lượng môn thi của mỗi thí sinh
# data['Số môn thi'] = data.count(axis=1) - 1  # Trừ cột SBD

# # Đếm số lượng thí sinh không thi đủ 6 môn
# students_not_enough_subjects = data[data['Số môn thi'] < 6]

# # Số lượng thí sinh không thi đủ 6 môn
# num_students_not_enough_subjects = students_not_enough_subjects.shape[0]

# # Số lượng thí sinh thi đủ 6 môn
# num_students_enough_subjects = len(data) - num_students_not_enough_subjects

# # Số lượng môn thi của mỗi thí sinh
# subjects_count = data['Số môn thi'].value_counts()

# # Vẽ biểu đồ cột với trục x là số môn thi và trục y là số lượng thí sinh
# plt.figure(figsize=(10, 6))
# plt.bar(subjects_count.index, subjects_count.values, color='skyblue')
# plt.xlabel('Số môn thi')
# plt.ylabel('Số lượng thí sinh')
# plt.title('Số lượng thí sinh theo số môn thi')
# plt.xticks(subjects_count.index)
# plt.grid(axis='y')
# plt.show()

# # Vẽ biểu đồ tròn là 2 phần là số lượng thí sinh thi đủ 6 môn và không đủ 6 môn
# labels = ['Đủ 6 môn', 'Không đủ 6 môn']
# sizes = [num_students_enough_subjects, num_students_not_enough_subjects]
# colors = ['lightgreen', 'lightcoral']
# explode = (0.1, 0)  # Tách phần "Đủ 6 môn" ra một chút

# plt.figure(figsize=(8, 8))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
#         shadow=True, startangle=140)
# plt.title('Tỉ lệ thí sinh thi đủ 6 môn và không đủ 6 môn')
# plt.axis('equal')  # Đảm bảo biểu đồ tròn
# plt.show()




####################
# import matplotlib.pyplot as plt
# import pandas as pd
# import os

# # Đọc file Excel
# file_path = '/mnt/data/diem_thi.xlsx'
# data = pd.read_excel(file_path)

# # Đếm số lượng môn thi của mỗi thí sinh
# data['Số môn thi'] = data.count(axis=1) - 1  # Trừ cột SBD

# # Đếm số lượng thí sinh không thi đủ 6 môn
# students_not_enough_subjects = data[data['Số môn thi'] < 6]

# # Số lượng thí sinh không thi đủ 6 môn
# num_students_not_enough_subjects = students_not_enough_subjects.shape[0]

# # Số lượng thí sinh thi đủ 6 môn
# num_students_enough_subjects = len(data) - num_students_not_enough_subjects

# # Số lượng môn thi của mỗi thí sinh
# subjects_count = data['Số môn thi'].value_counts()

# # Lưu biểu đồ vào cùng thư mục với file code này
# current_directory = os.path.dirname(os.path.abspath(__file__))

# # Vẽ biểu đồ cột với trục x là số môn thi và trục y là số lượng thí sinh
# plt.figure(figsize=(10, 6))
# plt.bar(subjects_count.index, subjects_count.values, color='skyblue')
# plt.xlabel('Số môn thi')
# plt.ylabel('Số lượng thí sinh')
# plt.title('Số lượng thí sinh theo số môn thi')
# plt.xticks(subjects_count.index)
# plt.grid(axis='y')
# # Lưu biểu đồ cột thành ảnh
# bar_chart_path = os.path.join(current_directory, 'so_mon_thi_vs_so_luong_thi_sinh.png')
# plt.savefig(bar_chart_path)
# plt.show()

# # Vẽ biểu đồ tròn là 2 phần là số lượng thí sinh thi đủ 6 môn và không đủ 6 môn
# labels = ['Đủ 6 môn', 'Không đủ 6 môn']
# sizes = [num_students_enough_subjects, num_students_not_enough_subjects]
# colors = ['lightgreen', 'lightcoral']
# explode = (0.1, 0)  # Tách phần "Đủ 6 môn" ra một chút

# plt.figure(figsize=(8, 8))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
#         shadow=True, startangle=140)
# plt.title('Tỉ lệ thí sinh thi đủ 6 môn và không đủ 6 môn')
# plt.axis('equal')  # Đảm bảo biểu đồ tròn
# # Lưu biểu đồ tròn thành ảnh
# pie_chart_path = os.path.join(current_directory, 'ti_le_thi_du_va_thi_khong_du_6_mon.png')
# plt.savefig(pie_chart_path)
# plt.show()

# bar_chart_path, pie_chart_path


import matplotlib.pyplot as plt
import pandas as pd
import os

# Đọc file Excel
file_path = 'diem_thi.xlsx'
data = pd.read_excel(file_path)

# Đếm số lượng môn thi của mỗi thí sinh
data['Số môn thi'] = data.count(axis=1) - 1  # Trừ cột SBD

# Đếm số lượng thí sinh không thi đủ 6 môn
students_not_enough_subjects = data[data['Số môn thi'] < 6]

# Số lượng thí sinh không thi đủ 6 môn
num_students_not_enough_subjects = students_not_enough_subjects.shape[0]

# Số lượng thí sinh thi đủ 6 môn
num_students_enough_subjects = len(data) - num_students_not_enough_subjects

# Số lượng môn thi của mỗi thí sinh
subjects_count = data['Số môn thi'].value_counts()

# Lưu biểu đồ vào cùng thư mục với file code này
bar_chart_path = 'so_mon_thi_vs_so_luong_thi_sinh.png'
pie_chart_path = 'ti_le_thi_du_va_thi_khong_du_6_mon.png'

# Vẽ biểu đồ cột với trục x là số môn thi và trục y là số lượng thí sinh
plt.figure(figsize=(10, 6))
bars = plt.bar(subjects_count.index, subjects_count.values, color='skyblue')
plt.xlabel('Số môn thi')
plt.ylabel('Số lượng thí sinh')
plt.title('Số lượng thí sinh theo số môn thi')
plt.xticks(subjects_count.index)
plt.grid(axis='y')

# Thêm số lượng thí sinh trên các cột
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom') # va='bottom' để hiển thị bên trên cột

plt.tight_layout()
# Lưu biểu đồ cột thành ảnh
plt.savefig(bar_chart_path)
plt.show()

# Vẽ biểu đồ tròn là 2 phần là số lượng thí sinh thi đủ 6 môn và không đủ 6 môn
labels = ['Đủ 6 môn', 'Không đủ 6 môn']
sizes = [num_students_enough_subjects, num_students_not_enough_subjects]
colors = ['lightgreen', 'lightcoral']
explode = (0.1, 0)  # Tách phần "Đủ 6 môn" ra một chút

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
plt.title('Tỉ lệ thí sinh thi đủ 6 môn và không đủ 6 môn')
plt.axis('equal')  # Đảm bảo biểu đồ tròn

# Lưu biểu đồ tròn thành ảnh
plt.savefig(pie_chart_path)
plt.show()
