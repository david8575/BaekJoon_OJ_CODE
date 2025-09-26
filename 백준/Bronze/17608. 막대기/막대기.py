import sys
input = sys.stdin.readline

sticks = []
n = int(input())
for _ in range(n):
    sticks.append(int(input()))

cnt = 0
min_height = 0
for i in range(n-1, -1, -1):
    if cnt == 0:
        cnt += 1
        min_height = sticks[i]
    
    elif sticks[i] > min_height:
        cnt += 1
        min_height = sticks[i]

print(cnt)