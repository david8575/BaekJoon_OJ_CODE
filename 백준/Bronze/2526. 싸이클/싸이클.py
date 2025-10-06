n, p = map(int, input().split())

seen_index = {} 
val = n
idx = 0

while True:
    val = (val * n) % p
    if val in seen_index:
        print(idx - seen_index[val])  
        break
    seen_index[val] = idx
    idx += 1