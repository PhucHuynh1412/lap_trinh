data = []
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        data_line = line.split(' - ')
        data.append(data_line)

date = data[0][0].split('-')
print(date[0])
if int(date[0]) < 7:
    print('Chua toi thang ')
else:
    print("da toi thang ")

