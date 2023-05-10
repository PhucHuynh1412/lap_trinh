import pyinputplus as pin 
import datetime
import sys
import numpy as np 

def menu():
    data = {1:'Nhập điểm',2:'Xem điểm',3:'Thoát'}
    for k, v in data.items():
        print(f'{k}. {v}.')
    print('*'*20)
    lua_chon_menu = pin.inputInt('Lựa chọn của Ba: ')
    return lua_chon_menu

def name():
    print('*'*20)
    data_name = {1: 'Mira', 2: 'Misu'}
    for k , v in data_name.items():
        print(f'{k}. {v}')
    lua_chon_name = pin.inputInt('Ba nhập điểm cho công chúa nào: ')
    if lua_chon_name == 1:
        return data_name[1]
    elif lua_chon_name == 2:
        return data_name[2]
    else:
        print('Ba chọn chưa đúng nhen!')
        name()

def nhap_diem(name):
    print('*'*20)
    diem = pin.inputInt(f'Nhập điểm của {name} là: ')
    noi_dung = pin.inputStr(f'Nhập thông tin điểm của {name} là: ')
    today = datetime.datetime.today().date().strftime('%A - %d/%m/%Y')
    data = [today, diem, noi_dung]
    data_end = {name:data}
    return data_end 

def ghi(data_end):
    for x in data_end:
        name = x
        data = data_end.get(x)
    with open(f'{name}.txt', 'a') as file:
        for item in data:
            file.write(str(item))
            file.write(" - ")
        file.write('\n')
    print('Done')

def xuat(name):
    diem = 0
    with open(f'{name}.txt', 'r') as file:
        for line in file.readlines():
            data_line = line.split(' - ')
            diem += int(data_line[2])
    print(f'Điểm của {name} là: {diem}')

def main():
    lua_chon = menu()
    if lua_chon == 1:
        n = name()
        data_end = nhap_diem(n)
        ghi(data_end)
        xuat(n)
    elif lua_chon == 3:
        sys.exit()
    elif lua_chon == 2:
        pass
    else:
        print('Ba chọn chưa đúng số!')
        main()

if __name__ == "__main__":
    main()
