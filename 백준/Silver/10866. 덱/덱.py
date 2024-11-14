from collections import deque

class Deque:
    def __init__(self):
        self.deque = deque()

    def push_front(self, data):
        self.deque.appendleft(data)

    def push_back(self, data):
        self.deque.append(data)

    def pop_front(self):
        if self.is_empty():
            return -1
        return self.deque.popleft()
    
    def pop_back(self):
        if self.is_empty():
            return -1
        return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def front(self):
        if self.is_empty():
            return -1
        return self.deque[0]
    
    def back(self):
        if self.is_empty():
            return -1
        return self.deque[-1]

# Deque 객체 생성
dq = Deque()

# 명령어 처리
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'push_front':
        dq.push_front(int(command[1]))
    elif command[0] == 'push_back':
        dq.push_back(int(command[1]))
    elif command[0] == 'pop_front':
        print(dq.pop_front())
    elif command[0] == 'pop_back':
        print(dq.pop_back())
    elif command[0] == 'size':
        print(dq.size())
    elif command[0] == 'empty':
        print(1 if dq.is_empty() else 0)
    elif command[0] == 'front':
        print(dq.front())
    elif command[0] == 'back':
        print(dq.back())
