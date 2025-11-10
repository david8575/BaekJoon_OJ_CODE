t = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(t):
    order = list(map(str, input()))
    h, w = 0, 0
    dir = 0 # 북 0, 서 1, 남 2, 동 3
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for i in order:
        if i == 'F':
            h += dy[dir]
            w += dx[dir]
        elif i == 'B':
            h -= dy[dir]
            w -= dx[dir]
        elif i == 'L':
            if dir == 3:
                dir = 0
            else:
                dir += 1
        elif i == 'R':
            if dir == 0:
                dir = 3
            else:
                dir -= 1 

        min_x = min(min_x, w)
        max_x = max(max_x, w)
        min_y = min(min_y, h)
        max_y = max(max_y, h)

    print(abs(max_x - min_x) * abs(max_y - min_y))