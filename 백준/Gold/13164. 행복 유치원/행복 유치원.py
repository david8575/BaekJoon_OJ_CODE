n, k = map(int, input().split())
kids = list(map(int, input().split()))

diff = []
for i in range(n-1):
    diff.append(kids[i+1] - kids[i])

diff.sort()
ans = 0
for i in range(n-k):
    ans += diff[i]

print(ans)