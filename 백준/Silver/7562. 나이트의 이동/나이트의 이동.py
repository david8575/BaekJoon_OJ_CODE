"""
1. 테스트 케이스 갯수 입력 받기
2. 
"""
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10*6)

t = int(input())

for _ in range(t):
    n = int(input())
    src_x, src_y = map(int, input().split())
    des_x, des_y = map(int, input().split())

    chess_board = [[0] * n for _ in range(n)]
    visited = [[False] * n  for _ in range(n)]

    q = deque()

    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    def bfs():
        q.append((src_x, src_y))
        visited[src_x][src_y] = True

        while q:
            x, y = q.popleft()

            if x == des_x and y == des_y:
                return 0
            
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if nx == des_x and ny == des_y:
                    visited[nx][ny] = True
                    return chess_board[x][y] + 1
                
                if visited[nx][ny] == False:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    chess_board[nx][ny] = chess_board[x][y] + 1
    
    print(bfs())