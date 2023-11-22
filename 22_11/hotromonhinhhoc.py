import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def tinh_khoang_cach(a, b):
    return np.linalg.norm(b - a)

def tinh_dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):
    if chieu_dai <= 0 or chieu_rong <= 0:
        raise ValueError("Chiều dài và chiều rộng phải lớn hơn 0.")
    return chieu_dai * chieu_rong

def tinh_chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong):
    return 2 * (chieu_dai + chieu_rong)

def tinh_dien_tich_hinh_vuong(canh):
    if canh <= 0:
        raise ValueError("Cạnh của hình vuông phải lớn hơn 0.")
    return canh ** 2

def tinh_dien_tich_hinh_tron(ban_kinh):
    if ban_kinh <= 0:
        raise ValueError("Bán kính của hình tròn phải lớn hơn 0.")
    return np.pi * ban_kinh ** 2

def tinh_the_tich_hinh_cau(ban_kinh):
    if ban_kinh <= 0:
        raise ValueError("Bán kính của hình cầu phải lớn hơn 0.")
    return (4 / 3) * np.pi * ban_kinh ** 3

def la_hinh_vuong(canh1, canh2):
    return canh1 == canh2

def ve_hinh_chu_nhat(chieu_dai, chieu_rong):
    fig, ax = plt.subplots()
    rect = patches.Rectangle((0, 0), chieu_dai, chieu_rong, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    plt.show()

# Ví dụ sử dụng các chức năng
diem_a = np.array([0, 0])
diem_b = np.array([3, 4])

khoang_cach = tinh_khoang_cach(diem_a, diem_b)
print(f"Khoảng cách giữa điểm A và B là: {khoang_cach}")

dien_tich_chu_nhat = tinh_dien_tich_hinh_chu_nhat(5, 8)
print(f"Diện tích hình chữ nhật là: {dien_tich_chu_nhat}")

chu_vi_chu_nhat = tinh_chu_vi_hinh_chu_nhat(5, 8)
print(f"Chu vi hình chữ nhật là: {chu_vi_chu_nhat}")

dien_tich_vuong = tinh_dien_tich_hinh_vuong(4)
print(f"Diện tích hình vuông là: {dien_tich_vuong}")

dien_tich_tron = tinh_dien_tich_hinh_tron(3)
print(f"Diện tích hình tròn là: {dien_tich_tron}")

the_tich_cau = tinh_the_tich_hinh_cau(3)
print(f"Thể tích hình cầu là: {the_tich_cau}")

print(f"Chữ nhật có phải là hình vuông không? {la_hinh_vuong(5, 8)}")

ve_hinh_chu_nhat(5, 8)
