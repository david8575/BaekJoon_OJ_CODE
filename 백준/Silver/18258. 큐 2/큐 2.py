import sys
from collections import deque

n = int(input())

d = deque([])

for i in range(n):
    order = sys.stdin.readline()
    order = order.split()
    
    if order[0] == "push":
        d.append(order[1])
    if order[0] == "pop":
        if len(d) == 0:
            print("-1")
        else:
            print(d.popleft())
    if order[0] == "size":
        print(len(d))
    if order[0] == "empty":
        if len(d) == 0:
            print('1')
        else:
            print('0')
    if order[0] == "front":
        if len(d) == 0:
            print("-1")
        else:
            print(d[0])
    if order[0] == "back":
        if len(d) == 0:
            print("-1")
        else:
            print(d[-1])