n = int(input())

ans = 1000
for _ in range(n):
    departure_time, bread_time = map(int, input().split())

    if departure_time <= bread_time:
        ans = min(bread_time, ans)

if ans == 1000:
    print(-1)
else:
    print(ans)