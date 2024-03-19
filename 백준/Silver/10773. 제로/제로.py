n = int(input())

list = []

for i in range(n):
    num = int(input())
    if num == 0:
        list.pop()
    else:
        list.append(num)
        
sum = 0
for i in range(len(list)):
    sum += list[i]
print(sum)