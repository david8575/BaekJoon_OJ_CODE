t = int(input())

for _ in range(t):
    M,N,x,y = map(int, input().split())
    
    if (M < N):
        M, N = N, M
        x, y = y, x
    
    check = False
    
    first = y
    for i in range(M):
        if first == x:
            print(y+i*N)
            check = True
            break
        
        first += N
        if first > M:
            first -= M
            
    if not check:
        print(-1)