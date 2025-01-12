n = int(input())
have = set(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

for i in range(m):
    if check[i] in have:
        print(1, end=" ")
    else:
        print(0, end=" ")