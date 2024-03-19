def hanoiTower(a,b,c,n):
    if (n == 1):
        print(a, c)
    else:
        hanoiTower(a,c,b,n-1)
        print(a, c)
        hanoiTower(b,a,c,n-1)

n = int(input())
a = 1
b = 2
c = 3

print(2**n-1)
if (n<=20):
    hanoiTower(a,b,c,n)