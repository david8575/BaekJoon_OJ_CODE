def gcd(a,b):
    if b == 0:
        return a 
    else:
        return gcd(b, a%b)
    
n, m = map(int, input().split())


print('1'*gcd(n,m))