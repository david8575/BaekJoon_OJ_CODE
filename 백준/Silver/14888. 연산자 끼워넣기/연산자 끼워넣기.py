import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -1e9
min_val = 1e9

def dfs(idx, result, plus, minus, mul, div):
    global max_val, min_val
    
    if idx == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return
    
    if plus > 0:
        dfs(idx + 1, result + num[idx], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, result - num[idx], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * num[idx], plus, minus, mul - 1, div)
    if div > 0:
        dfs(idx + 1, int(result / num[idx]), plus, minus, mul, div - 1)

dfs(1, num[0], plus, minus, mul, div)

print(int(max_val))
print(int(min_val))
