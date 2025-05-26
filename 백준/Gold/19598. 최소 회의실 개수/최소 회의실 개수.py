from queue import PriorityQueue
n = int(input())
courses = []

for _ in range(n):
    src , des = map(int, input().split())
    courses.append((src, des))

courses.sort()
count = 1

pq = PriorityQueue()
pq.put(courses[0][1])

for i in range(1, n):
    a = pq.get()

    if a <= courses[i][0]:
        pq.put(courses[i][1])
    else:
        count += 1
        pq.put(courses[i][1])
        pq.put(a)

print(count)