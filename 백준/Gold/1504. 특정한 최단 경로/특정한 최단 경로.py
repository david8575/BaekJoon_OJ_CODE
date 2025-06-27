import heapq

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    src, des, cost = map(int, input().split())
    graph[src].append((cost, des))
    graph[des].append((cost, src))

v1, v2 = map(int, input().split())

def dijkstra(src, des, graph):
    distance = [float('inf') for _ in range(n+1)]
    distance[src] = 0
    pq = [(0, src)]

    while pq:
        cost, node = heapq.heappop(pq)

        if distance[node] < cost:
            continue

        for adj_cost, adj_node in graph[node]:
            new_cost = distance[node] + adj_cost

            if new_cost < distance[adj_node]:
                distance[adj_node] = new_cost
                heapq.heappush(pq, (new_cost, adj_node))

    return distance[des]

d1 = dijkstra(1, v1, graph) + dijkstra(v1, v2, graph) + dijkstra(v2, n, graph)
d2 = dijkstra(1, v2, graph) + dijkstra(v2, v1, graph) + dijkstra(v1, n, graph)
    
if d1 == float('inf') or d2 == float('inf'):
    print(-1)
else:
    print(min(d1, d2))