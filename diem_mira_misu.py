import pyinputplus as pin 
import datetime

def menu():
    data = {1:'Nhập điểm',2:'Xem điểm',3:'Thoát'}
    for k, v in data.items():
        print(f'{k}. {v}.')
    print('*'*20)
    lua_chon = pin.inputInt('Lựa chọn của ông xã: ')
    return lua_chon

def nhap_diem(name):
 = pin.inputInt(f'Nhập điểm của {name} là ')
    noi_dung = pin.inputStr(f'Nhập thông tin điểm của {name} là: ')
    today = datetime.datetime.today().date().strftime('%A - %d/%m/%Y')
    data = [today, diem, noi_dung]
    return data 

def main():
    lua_chon = menu()
    data = nhap_diem('Mira')
    print(data)

if __name__ == "__main__":
    main()

