m, n = map(int, input().split())
list1 = [i for i in range(1, m+1)]
for i in range(n):
    a, b = map(int, input().split())
    temp_area = list1[a-1:b]
    temp_area.reverse()
    list1[a-1:b] = temp_area
for i in list1:
    print(i, end=" ")