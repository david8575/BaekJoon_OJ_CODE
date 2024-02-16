n = int(input())
cord_list = []
for i in range(n):
    cord = list(map(int, input().split()))
    cord_list.append(cord)
cord_list.sort()
for i in range(n):
    print(cord_list[i][0], end=" ")
    print(cord_list[i][1])