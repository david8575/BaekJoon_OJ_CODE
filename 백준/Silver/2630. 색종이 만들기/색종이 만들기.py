import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0

def func(x, y, n):
    global w, b

    tmp = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] == 1:
                tmp += 1

    if not tmp:
        w += 1
    elif tmp == n**2:
        b += 1
    else:
        func(x, y, n//2)
        func(x, y+n//2, n//2)
        func(x+n//2, y, n//2)
        func(x+n//2, y+n//2, n//2)

func(0, 0, n)
print(w)
print(b)