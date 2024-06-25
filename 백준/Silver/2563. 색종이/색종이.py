drawingPage = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for dx in range(x, x+10):
        for dy in range(y, y+10):
            drawingPage[dx][dy]+=1

cnt = 0
for i in range(100):
    for j  in range(100):
        if drawingPage[i][j] > 1:
            cnt+= drawingPage[i][j]-1

print(n*100-cnt)