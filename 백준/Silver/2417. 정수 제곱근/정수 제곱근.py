n = int(input())
low = 0
high = 2**32

while(low <= high):
    mid = (high+low) // 2
    if mid**2 < n:
        low = mid+1
    else:
        high = mid-1

print(high+1)