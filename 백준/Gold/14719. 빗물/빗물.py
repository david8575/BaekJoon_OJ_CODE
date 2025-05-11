h, w = map(int, input().split())
stc = list(map(int, input().split()))

map = [[0] * w for _ in range(h)]

for i in range(w):
    for j in range(stc[i]):
        map[h-1-j][i] = 1

count = 0
for i in range(h):
    for j in range(w):
        if map[i][j] == 1:
            continue

        k = j
        while k >= 0:
            if map[i][k] == 1:
                break
            k-=1
        if k == -1:
            continue

        k = j
        while k < w:
            if map[i][k] == 1:
                break
            k+=1
        if k == w:
            continue

        count+=1

print(count)