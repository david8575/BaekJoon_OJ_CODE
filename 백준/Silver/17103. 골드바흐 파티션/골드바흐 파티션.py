def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_num + 1, i):
                is_prime[j] = False
    return is_prime

def count_goldbach_partitions(n, is_prime):
    count = 0
    for i in range(2, n//2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1
    return count

t = int(input())
max_n = 1000000
is_prime = sieve(max_n)

for _ in range(t):
    n = int(input())
    print(count_goldbach_partitions(n, is_prime))