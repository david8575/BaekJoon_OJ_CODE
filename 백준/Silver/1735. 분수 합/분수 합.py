import math

a, b = map(int, input().split())
c, d = map(int, input().split())

son = a * d + c * b
mom = b * d

div = math.gcd(son, mom)
print(f"{son // div} {mom // div}")