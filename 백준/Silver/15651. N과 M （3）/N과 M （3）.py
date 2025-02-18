from itertools import product

n, m = map(int, input().split())

nums = [i+1 for i in range(n)]

for pro in product(range(n), repeat=m):
    pro = list(pro)
    for i in pro:
        print(i+1, end=" ")

    print()