import pyinputplus as pin 
from datetime import datetime

def input_data():
    salary = pin.inputInt("Nhập lương: ")
    salary_real = pin.inputInt("Nhập tiền còn lại sau khi trừ phí: ")
    investment_money = pin.inputInt("Tiền đầu tư: ")
    money_left_over = pin.inputInt("Tiền dư cuối tháng: ")
    return salary, salary_real, investment_money, money_left_over

def write_data(data):
    pass 

def main():
    data = []
    data = input_data()
    print(data)

if __name__ == "__main__":
    main()

