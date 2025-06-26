import heapq
n, k = map(int, input().split())

time = [float('inf') for _ in range(100001)]
time[n] = 0

pq = [(0, n)] 

while pq:
    cost, node = heapq.heappop(pq)
    if node == k:
        print(cost)
        break

    if cost > time[node]:
        continue

    if 0 <= node*2 <= 100000 and time[node*2] > cost:
        time[node*2] = cost
        heapq.heappush(pq, (cost, node*2))

    if 0 <= node-1 <= 100000 and time[node-1] > cost+1:
        time[node-1] = cost+1
        heapq.heappush(pq, (cost+1, node-1))

    if 0 <= node+1 <= 100000 and time[node+1] > cost+1:
        time[node+1] = cost+1
        heapq.heappush(pq, (cost+1, node+1))

   