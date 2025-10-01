
import sys
input=sys.stdin.readline

n = int(input())

balls = []

for i in range(n):
    color, size = map(int, input().split())
    balls.append((size, color, i))

balls.sort()
color_count = [0] * 200001
total_count = 0
cnt = 0
points = [0] * (n+1)

for i in range(n):
    while balls[cnt][0] < balls[i][0]:
        color_count[balls[cnt][1]] += balls[cnt][0]
        total_count += balls[cnt][0]
        cnt += 1
    points[balls[i][2]] = total_count - color_count[balls[i][1]]

for i in range(n):
    print(points[i])