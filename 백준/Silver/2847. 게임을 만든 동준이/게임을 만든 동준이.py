n = int(input())

level = [0]*n

for i in range(n):
    level[i] = int(input())

count = 0
for i in range(n-2, -1, -1):
    if level[i] >= level[i+1]:
        count += level[i] -(level[i+1] - 1)
        level[i] = level[i+1]-1
        
print(count)