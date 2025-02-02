import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

deq = deque(enumerate(map(int, input().split())))
answer = []

while deq:
    idx, num = deq.popleft()
    answer.append(idx + 1)
    
    if num > 0:
        deq.rotate(-(num-1))
    else:
        deq.rotate(-num)

print(*answer)