import math
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    print((n*m) // math.gcd(n,m))
    