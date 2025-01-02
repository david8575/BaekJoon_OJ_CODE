n = int(input())

div = 2
while(True):
    if n == 1:
        break
    
    if n % div == 0:
        print(div)
        n = n // div
    else:
        div += 1