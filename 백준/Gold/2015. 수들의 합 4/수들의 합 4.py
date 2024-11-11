n, k = map(int, input().split())

nums = list(map(int, input().split()))

prefix_num = []
prefix_num.append(nums[0])

for i in range(1, n):
    prefix_num.append(prefix_num[i-1]+nums[i])
    
answer = 0
count = {}    
for i in range(n):
    goal = prefix_num[i] - k
    
    if goal == 0:
        answer += 1
    
    if goal in count:
        answer += count[goal]
    
    if prefix_num[i] not in count:
        count[prefix_num[i]] = 0
    count[prefix_num[i]] += 1
    
print(answer)