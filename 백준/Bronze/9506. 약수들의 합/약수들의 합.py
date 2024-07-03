while True:
    n = int(input())
    if n != -1:
        result = 0
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                result += i
                divisors.append(i)
        if n == result:
            print(f'{n} = ' + ' + '.join(map(str, divisors)))
        else:
            print(f'{n} is NOT perfect.')
    else:
        break
