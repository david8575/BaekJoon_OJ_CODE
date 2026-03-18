n = int(input())
senior = list(map(int, input().split()))
children = [[] for _ in range(n)]

root = -1
for i in range(n):
    if senior[i] == -1:
        root = i
    else:
        children[senior[i]].append(i)

def dfs(v):
    if not children[v]:
        return 0
    
    child_times = [dfs(c) for c in children[v]]
    child_times.sort(reverse=True)

    result = 0
    
    for i, t in enumerate(child_times):
        result = max(result, i+1+t)

    return result

print(dfs(root))