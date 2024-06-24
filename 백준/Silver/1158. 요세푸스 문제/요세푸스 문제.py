from collections import deque

def josephus_problem(n, k):
    circle = deque(range(1, n+1))
    result = []

    while circle:
        circle.rotate(-k+1)
        result.append(circle.popleft())

    return result

n, k = map(int, input().split())

result = josephus_problem(n,k)

print("<" + ", ".join(map(str, result)) + ">")

