city = int(input())
request = list(map(int, input().split()))
budget = int(input())
lower_limit = 0
upper_limit = max(request)
answer = -1
while lower_limit <= upper_limit:
    mid = (lower_limit + upper_limit) // 2
    sum = 0
    for i in range(city):
        sum += min(mid, request[i])
        
    if sum <= budget:
        answer = mid
        lower_limit = mid + 1
    else:
        upper_limit = mid - 1

print(answer)   