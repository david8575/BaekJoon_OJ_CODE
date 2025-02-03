from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

queue = deque([])
for i in range(n):
    if a[i] == 0: 
        queue.append(b[i])

for i in range(m):
    queue.appendleft(c[i])
    print(queue.pop(), end= ' ')