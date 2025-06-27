import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    src, des, cost = map(int, input().split())
    graph[src-1].append((des-1, cost))

def dijkstra(start):
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
            
        for next_node, cost in graph[current_node]:
            new_dist = current_dist + cost
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return distances

x_to_home = dijkstra(x-1)

reverse_graph = [[] for _ in range(n)]
for i in range(n):
    for j, cost in graph[i]:
        reverse_graph[j].append((i, cost))

def reverse_dijkstra(start):
    distances = [float('inf')] * n
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > distances[current_node]:
            continue
            
        for next_node, cost in reverse_graph[current_node]:
            new_dist = current_dist + cost
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    
    return distances

come_to_x = reverse_dijkstra(x-1)

ans = [come_to_x[i] + x_to_home[i] for i in range(n)]
print(max(ans))