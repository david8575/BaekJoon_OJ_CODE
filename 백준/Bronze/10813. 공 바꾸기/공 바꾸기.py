m, n = map(int, input().split())
list1 = []
for i in range(0, m): list1.append(i+1)
for i in range(0, n):
    i, j = map(int, input().split())
    temp = list1[i-1]
    list1[i-1] = list1[j-1]
    list1[j-1] = temp
for i in list1:
    print(i, end=" ")