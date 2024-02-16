list1 = []
for i in range(5):
    a = int(input())
    list1.append(a)

list1.sort()
sum = 0
for i in range(len(list1)):
    sum+=list1[i]
print(sum//5)
print(list1[2])