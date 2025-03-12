t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    important = list(map(int, input().split()))

    result = 1
    while important:
        if important[0] < max(important):
            important.append(important.pop(0))
        else:
            if m == 0: 
                break

            important.pop(0)
            result += 1
        
        m = m - 1 if m > 0 else len(important) - 1

    print(result) 