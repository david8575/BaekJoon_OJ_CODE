def find_smallest_constructor(N):
    for i in range(1, N + 1):
        decomposition_sum = i + sum(map(int, str(i)))
        if decomposition_sum == N:
            return i
    return 0

N = int(input())
print(find_smallest_constructor(N))