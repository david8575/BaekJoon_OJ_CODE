n = int(input())
m = int(input())

adj = [[] for _ in range(n)]

for _ in range(m):
    src, des = map(int, input().split())
    adj[src-1].append(des-1)
    adj[des-1].append(src-1)
    
friend = [0]*n

for i in adj[0]:
    friend[i] = 1
    
friend_friend = [0]*n

for i in range(n):
    if friend[i]==0:
        continue
    for j in adj[i]:
        if j != 0 and friend[j] == 0:
            friend_friend[j]=1
            
print(sum(friend) + sum(friend_friend))