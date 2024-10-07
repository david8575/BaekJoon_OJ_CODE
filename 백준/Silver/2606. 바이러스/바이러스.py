com = int(input())
connect = int(input())

graph = [[] for _ in range(com)]

for _ in range(connect):
    src, des = map(int, input().split())
    graph[src-1].append(des-1)
    graph[des-1].append(src-1)
    
check = [0] * com
check[0] = 1

while True:
    new = False
    
    for i in range(com):
        if check[i] == 0: 
           continue
       
        for j in graph[i]:
            if check[j] == 0:
                check[j] = 1
                new = True
    if not new:    
        break

print(check.count(1)-1)