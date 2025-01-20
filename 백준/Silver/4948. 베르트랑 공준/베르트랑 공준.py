def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_num + 1, i):
                is_prime[j] = False

    return is_prime

max_num = 123456 * 2
prime_list = sieve(max_num)

while True:
    num = int(input())

    if num == 0:
        break

    count = sum(prime_list[num + 1:2*num + 1])
    print(count)
