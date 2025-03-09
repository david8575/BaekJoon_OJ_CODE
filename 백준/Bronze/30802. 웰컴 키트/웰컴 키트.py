n = int(input())
people = list(map(int, input().split()))
t, p = map(int, input().split())

t_shirt = 0
for i in people:
    if i == 0:
        continue
    elif i <= t:
        t_shirt += 1
    elif i%t==0:
        t_shirt+=i//t
    else:
        t_shirt += (i//t+1)


print(t_shirt)
print(n // p, n % p)
