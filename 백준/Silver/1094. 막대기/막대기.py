n = int(input())
stick = 64
count = 0
while n > 0:
    if stick > n:
        stick //= 2
    else :
        n -= stick
        count += 1
print(count)