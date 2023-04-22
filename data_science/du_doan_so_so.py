import numpy as np
from sklearn.linear_model import LinearRegression

def so_don_vi():
    #TODO: Khởi tạo dữ liệu đầu vào
    X = np.array(range(11)).reshape((-1, 1))
    y = np.array([9,8,5,0,9,5,4,1,6,8,2])

    #TODO: Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    model.fit(X, y)

    #TODO: Dự đoán giá trị tiếp theo trong dãy số
    X_new = np.array([12]).reshape((-1, 1))
    y_new = model.predict(X_new)

    print("Giá trị tiếp theo hàng đơn vị:", y_new[0])
    return int(round(y_new[0],0))

def so_hang_chuc():
    #TODO: Khởi tạo dữ liệu đầu vào
    X = np.array(range(11)).reshape((-1, 1))
    y = np.array([2,9,0,6,2,6,0,9,7,6,4])

    #TODO: Tạo mô hình hồi quy tuyến tính
    model = LinearRegression()
    model.fit(X, y)

    #TODO: Dự đoán giá trị tiếp theo trong dãy số
    X_new = np.array([12]).reshape((-1, 1))
    y_new = model.predict(X_new)

    print("Giá trị tiếp theo hàng chục:", y_new[0])
    return int(round(y_new[0],0))

def main():
    dv = so_don_vi()
    hc = so_hang_chuc()
    print(f'Số tiếp theo của ngày mai có 2 chữ số là: {hc}{dv}')

if __name__ == "__main__":
    main()
