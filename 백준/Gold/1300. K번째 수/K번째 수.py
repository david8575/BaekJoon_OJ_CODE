n = int(input())
k = int(input())

low = 1
high = n*n
answer = -1

while low <= high:
    mid = (low+high) // 2

    count = 0
    for i in range(1, n+1):
        count += min(n, (mid-1) // i)

    if count < k:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)