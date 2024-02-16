n = (input())
list1 = []
for i in range(len(n)):
    list1.append(n[i])
list1.sort()
for i in range(len(list1)):
    print(list1[len(list1)-i-1],end="")