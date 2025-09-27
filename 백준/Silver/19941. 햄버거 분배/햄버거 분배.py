n, k = map(int, input().split())
pos = list(input())

cnt = 0
for i in range(n):
    if pos[i] == 'P':
        for j in range(max(0, i-k), min(n, i+k+1)):
            if pos[j] == 'H':
                cnt+=1
                pos[j] = 'X'
                break

print(cnt)
