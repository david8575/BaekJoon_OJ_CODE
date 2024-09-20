from itertools import permutations

n = int(input())
num = list(map(int, input().split()))

cases = permutations(num)

answer = 0
for c in cases:
    total = 0
    for i in range(len(c)-1):
        total += abs(c[i] - c[i+1])
        if answer < total:
            answer = total
            
print(answer)