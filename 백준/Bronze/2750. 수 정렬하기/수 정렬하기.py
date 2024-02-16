n = int(input())
list1 = []
for i in range(n):
    a = int(input())
    if a not in list1:
        list1.append(a)
list1.sort()
for i in range(len(list1)):
    print(list1[i])