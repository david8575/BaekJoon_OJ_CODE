n = int(input())

a = [0] * 1002
a[1] = 1
a[2] = 2
for i in range(3,n+1):
    a[i] = a[i-1] + a[i-2]
    a[i] %= 10007
print(a[n])