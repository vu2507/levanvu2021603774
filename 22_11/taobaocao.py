import pandas as pd

# Đường link đến file CSV trên GitHub
url = "/content/bangdiempython.csv"

# Đọc dữ liệu từ file CSV
data = pd.read_csv(url)

# Kiểm tra và thêm các cột L1, L2, TX1, TX2 nếu chưa tồn tại
for col in ['L1', 'L2', 'TX1', 'TX2']:
    if col not in data.columns:
        data[col] = 0

# Tính toán các thông số cuối kỳ
data['Cuoi ky'] = data[['L1', 'L2', 'TX1', 'TX2']].sum(axis=1)
data['Diem Trung Binh'] = data['Cuoi ky'] / 4.0

# Tính tỷ lệ sinh viên qua môn
def tinh_ty_le_qua_mon(row):
    diem_cuoi_ky = row['Cuoi ky']
    if diem_cuoi_ky >= 5:
        return 'Qua môn'
    else:
        return 'Không qua môn'

data['Tinh Trang'] = data.apply(tinh_ty_le_qua_mon, axis=1)

# Tạo báo cáo
bao_cao = data[['STT', 'Ma lop', 'Ma SV', 'L1', 'L2', 'TX1', 'TX2', 'Cuoi ky', 'Diem Trung Binh', 'Tinh Trang']]
print(bao_cao)
