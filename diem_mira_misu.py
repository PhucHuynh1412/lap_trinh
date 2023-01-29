import pyinputplus as pin 
import datetime

def menu():
    data = {1:'Nhập điểm',2:'Xem điểm',3:'Thoát'}
    for k, v in data.items():
        print(f'{k}. {v}.')
    print('*'*20)
    lua_chon_menu = pin.inputInt('Lựa chọn của Ba: ')
    return lua_chon_menu

def name():
    data_name = {1: 'Mira', 2: 'Misu'}
    for k , v in data_name.items():
        print(f'{k}. {v}')
    lua_chon_name = pin.inputInt('Ba nhập điểm cho công chúa nào: ')
    if lua_chon_name == 1:
        return data_name[1]
    elif lua_chon_name == 2:
        return data_name[2]

def nhap_diem(name):
    diem = pin.inputInt(f'Nhập điểm của {name} là ')
    noi_dung = pin.inputStr(f'Nhập thông tin điểm của {name} là: ')
    today = datetime.datetime.today().date().strftime('%A - %d/%m/%Y')
    data = [today, diem, noi_dung]
    data_end = {name:data}
    return data_end 

def ghi(data_end):
    for x in data_end:
        name = x
        data = data_end.get(x)
    print(x)
    print(data)
        
def main():
    lua_chon = menu()
    data = nhap_diem('Mira')
    print(data)
    ghi(data)

if __name__ == "__main__":
    main()

