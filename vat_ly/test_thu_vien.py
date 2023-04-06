import numpy as np 

#TODO: Tao ma tran 
A = np.array([[2,3],[4,-1]])

B = np.array([8,2])

#TODO: Giai he phuong trinh 2 an
result = np.linalg.solve(A,B)

print(f"ket qua x va y la: {result}")
