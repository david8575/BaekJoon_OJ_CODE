n, m = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
start = 0
end = 0
sum = nums[0]

while(1):
    if sum == m:
        count+=1
        
    if sum >= m:
        start+=1
        sum -= nums[start-1]
    else:
        if end == n-1:
            break
        end+=1
        sum += nums[end]
print(count)