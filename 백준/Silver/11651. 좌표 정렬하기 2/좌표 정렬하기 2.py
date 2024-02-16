n = int(input())
cord_list = []
for i in range(n):
    cord = list(map(int, input().split()))
    temp = cord[0]
    cord[0] = cord[1]
    cord[1] = temp
    cord_list.append(cord)
cord_list.sort()
for i in range(n):
    print(cord_list[i][1], end=" ")
    print(cord_list[i][0])