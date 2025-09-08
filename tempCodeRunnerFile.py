from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load mô hình đã lưu
mo_hinh = joblib.load("mo_hinh_rf.pkl")

# Các đặc trưng cần thiết
dac_trung_quan_trong = [
    "concave points_mean",
    "concave points_worst",
    "area_worst",
    "concavity_mean",
    "radius_worst"
]

# Hàm dự đoán
def du_doan_khoi_u(dau_vao):
    df = pd.DataFrame([dau_vao], columns=dac_trung_quan_trong)
    ket_qua = mo_hinh.predict(df)
    return "LÀNH TÍNH ✅" if ket_qua[0] == 1 else "ÁC TÍNH ❌"

@app.route("/", methods=["GET", "POST"])
def index():
    ket_qua = None
    gia_tri_nhap = {ten: "" for ten in dac_trung_quan_trong}

    if request.method == "POST":
        try:
            dau_vao = []
            for ten in dac_trung_quan_trong:
                val = request.form.get(ten, "")
                gia_tri_nhap[ten] = val
                dau_vao.append(float(val))
            ket_qua = du_doan_khoi_u(dau_vao)
        except ValueError:
            ket_qua = "⚠️ Dữ liệu không hợp lệ!"

    return render_template("index.html",
                           dac_trung_quan_trong=dac_trung_quan_trong,
                           gia_tri_nhap=gia_tri_nhap,
                           ket_qua=ket_qua)

if __name__ == "__main__":
    app.run(debug=True)
