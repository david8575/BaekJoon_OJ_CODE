def n_queens(k):
    global n, cnt

    if k==n:
        cnt+=1
        return

    for i in range(n):
        if not used_c[i] and not used_up[k+i] and not used_down[(n-1)+k-i]:
            used_c[i] = True
            used_up[k+i] = True
            used_down[(n-1)+k-i] = True
            n_queens(k+1)
            used_c[i] = False
            used_up[k+i] = False
            used_down[(n-1)+k-i] = False

n = int(input())
used_c = [False]*n
used_up = [False]*(2*(n-1)+1)
used_down = [False]*(2*(n-1)+1)
cnt = 0
n_queens(0)
print(cnt)