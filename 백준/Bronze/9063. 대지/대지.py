x_list = []
y_list = []
max_x, max_y, min_x, min_y = 0, 0, 0, 0
spots = int(input())
for i in range(spots):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
max_x = max(x_list)
min_x = min(x_list)
max_y = max(y_list)
min_y = min(y_list)
print((max_x-min_x)*(max_y-min_y))