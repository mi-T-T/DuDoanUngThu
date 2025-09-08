# 🩺 Ứng dụng Dự Đoán Ung Thư Vú

Ứng dụng web đơn giản để dự đoán khối u vú là **lành tính** hay **ác tính** dựa trên dữ liệu xét nghiệm. Mô hình học máy sử dụng là **Random Forest**.

---

## 🚀 Tính năng

- Nhập 5 đặc trưng xét nghiệm:
  
    `concave points_mean`(Trung bình số điểm lõm)
  
    `concave points_worst`(Số điểm lõm nhiều nhất)
  
    `area_worst`(Diện tích lớn nhất)
  
    `concavity_mean`(Trung bình độ lõm)
  
    `radius_worst`(Bán kính lớn nhất)
- Dự đoán khối u là **LÀNH TÍNH** ✅ hoặc **ÁC TÍNH** ❌

---

## 🧰 Công nghệ sử dụng
- Python 3
- Flask
- Bootstrap 5

---
## ✨ Giao diện
<img width="1296" height="630" alt="image" src="https://github.com/user-attachments/assets/d5296e17-f898-42e8-8ad1-a5ed74bf7e15" />
<img width="1295" height="624" alt="image" src="https://github.com/user-attachments/assets/9dff75d3-ad31-4451-80b3-8b135782ab70" />

---

## 🧠 Mô hình học máy

- **Thuật toán**: RandomForestClassifier
- **Thư viện**: scikit-learn
- **Đặc trưng sử dụng**: 5 đặc trưng quan trọng nhất được chọn từ bộ dữ liệu bao gồm `concave points_mean`, `concave points_worst`, `area_worst`, `concavity_mean`, `radius_worst`
- **Độ chính xác**: phát hiện ra được 92% ca bệnh ung thư vú

---

## ⚙️ Cài đặt & chạy ứng dụng

### Clone dự án
```bash
git clone https://github.com/mi-T-T/DuDoanUngThu.git
cd DuDoanUngThu
