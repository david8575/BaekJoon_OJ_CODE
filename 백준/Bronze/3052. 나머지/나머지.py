num_list = []

for i in range(10):
    a = int(input())
    if (a%42) not in num_list:
        num_list.append(a%42)

print(len(num_list))