n = int(input())

ropes = []
for _ in range(n):
    ropes.append(int(input()))
    
ropes.sort(reverse=True)

max = 0
for i in range(n):
    if max < ropes[i] * (i+1):
        max = ropes[i] * (i+1)
        
print(max)