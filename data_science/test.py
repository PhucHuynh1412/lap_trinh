import random

# Dãy số đã biết
known_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Tính toán xác suất xuất hiện của từng số trong dãy số
probability_distribution = [1/len(known_sequence) for _ in range(len(known_sequence))]

# Dự đoán số tiếp theo dựa trên xác suất xuất hiện của từng số
next_number = random.choices(known_sequence, weights=probability_distribution)[0]

# Hiển thị số tiếp theo được dự đoán
print("Số tiếp theo trong dãy số là:", next_number)
