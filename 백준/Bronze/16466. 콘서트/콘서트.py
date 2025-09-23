n = int(input())
first_res = sorted(list(map(int, input().split())))
check = True

for i in range(n):
    if i+1 != first_res[i]:
        print(i+1)
        check = False
        break

if check:
    print(n+1)