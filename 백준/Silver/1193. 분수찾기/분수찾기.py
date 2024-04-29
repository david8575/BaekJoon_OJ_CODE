n = int(input())
i = 1
while(n > i):
    n = n - i
    i += 1

if (i % 2== 0):
    print(f'{n}/{i-n+1}')
else:
    print(f'{i-n+1}/{n}')