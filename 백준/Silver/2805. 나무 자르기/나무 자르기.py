n, m = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
answer = -1

while low <= high:
    mid = (high+low) // 2
    
    sum = 0
    for tree in trees:
        sum += max(0, (tree-mid))
        
    if sum >= m:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)