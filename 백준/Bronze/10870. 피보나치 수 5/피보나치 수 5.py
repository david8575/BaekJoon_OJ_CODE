def fibonacci_1(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_1(num-1) + fibonacci_1(num-2)
    
n = int(input())
print(fibonacci_1(n))