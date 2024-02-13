n = 1
for i in range(3):
    n *= int(input())
num_list = []
for i in range(len(str(n))):
    num_list.append(str(n)[i])
dic = {"0":0, "1":0, "2":0, "3":0, "4":0,
       "5":0, "6":0, "7":0, "8":0, "9":0,}
for i in num_list:
    count = 0
    for j in num_list:
        if j == i:
            count += 1
    dic[i] = str(count)
for i in range(10):
    print(dic[str(i)])