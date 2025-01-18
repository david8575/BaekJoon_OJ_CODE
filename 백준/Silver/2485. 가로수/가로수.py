import math
n = int(input())

a = int(input())

arr = []

for i in range(n-1):
    num = int(input())
    arr.append(num-a)
    a = num

b = arr[0]

for j in range(1, len(arr)):
    b = math.gcd(b, arr[j])

result = 0
for each in arr:
    result += each//b-1

print(result) 