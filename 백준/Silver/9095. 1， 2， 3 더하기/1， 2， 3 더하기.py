t = int(input())

def func(n):
    if n == 1: 
        return 1 
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return func(n-1) + func(n-2) + func(n-3)

for _ in range(t):
    n= int(input())
    print(func(n))