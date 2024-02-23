def eratosthenes(num1, num2):
    count_primes = [True] * (num2+1)
    count_primes[0] = False
    count_primes[1] = False

    for i in range(2, int(num2**0.5)+1):
        if count_primes[i]:
            for j in range(i*i, num2+1, i):
                count_primes[j] = False
    
    primes = []
    for i in range(num1, num2+1):
        if count_primes[i]:
            primes.append(i)
    for i in range(len(primes)):
        print(primes[i])

m, n = map(int,input().split())
eratosthenes(m, n)