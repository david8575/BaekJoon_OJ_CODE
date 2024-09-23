for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    main = 0
    sub = 0
    count = 0
    
    while main < n:
        if sub == m:
            count+=sub
            main+=1
        else:
            if a[main] > b[sub]:
                sub+=1
            else:
                count+=sub
                main+=1
                
    print(count)