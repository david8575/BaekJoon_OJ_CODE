import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan = []
for _ in range(k):
    lan.append(int(input()))

low, high = 1, max(lan)

while(low <= high):
    mid = (low + high) // 2
    lan_cut = 0

    for line in lan:
        lan_cut += line // mid
        
    if lan_cut >= n:
        low = mid + 1
    else:
        high = mid - 1
    
print(high)