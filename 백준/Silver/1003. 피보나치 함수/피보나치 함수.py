def fibonacci_count(n):
    cnt = [(1,0), (0,1)] + [(0,0)] * (n-1)
    for i in range(2,n+1):
        cnt[i] = (cnt[i-1][0] + cnt[i-2][0], cnt[i-1][1] + cnt[i-2][1])
    return cnt[n]

n = int(input())

for i in range(n):
    num = int(input())
    zero, one = fibonacci_count(num)
    print(f"{zero} {one}")