from collections import deque

n = int(input())

list = []
for i in range(n):
    list.append(i+1)
list = deque(list)
for i in range(n-1):
    list.popleft()
    list.append(list.popleft())
    
print(list[0])