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

def main():
    bs, ms, ns, ss = input()
    salary = salary_caculation(bs,ms,ns,ss)
    print(f"Lương tháng này là: {salary}")

if __name__ == "__main__":
    main()

