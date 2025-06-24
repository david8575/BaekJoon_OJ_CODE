import heapq

n = int(input())
q = []

for _ in range(n):
    nums = list(map(int, input().split()))

    for num in nums:
        if len(q) < n:
            heapq.heappush(q, num)
        else:
            if q[0] < num:
                heapq.heappush(q, num)
                heapq.heappop(q)
print(q[0])
