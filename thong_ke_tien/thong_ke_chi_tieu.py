import pyinputplus as pin 

def input():
    bs = pin.inputInt('Nhập mức lương cơ bản: ')
    ms = pin.inputInt('Nhập số ca sáng trong 1 tuần: ')
    ns = pin.inputInt('Nhập số ca tối trong 1 tuần: ')
    ss = pin.inputInt('Nhập số ca trong chủ nhật trong 1 tuần: ')
    return bs, ms, ns, ss 

def salary_caculation(bs,ms,ns,ss):
    mss = bs 
    nss = bs + 40
    sss = bs + 60 
    salary = (ms*mss + ns*nss + ss*sss)*4
    return salary

def spending_for_the_month():
    bank_debt = 9100
    parent_money = 2000
    english_money = 1000
    money_for_children = 1800
    telephone_fee = 500
    return [bank_debt, parent_money, english_money, money_for_children, telephone_fee]

def cash_in_return(salary):
    data = spending_for_the_month()
    salary_real = salary
    for num in data:
        salary_real = salary_real - num 
    return salary_real

def main():
    bs, ms, ns, ss = input()
    salary = salary_caculation(bs,ms,ns,ss)
    print(f"Lương tháng này là: {salary}")
    investment_money = pin.inputInt('Nhập tiền đầu tư tháng này: ')
    salary_real = cash_in_return(salary) - investment_money
    print(f"Tiền còn lại sau khi trừ các khoảng phí là: {salary_real}")

if __name__ == "__main__":
    main()

