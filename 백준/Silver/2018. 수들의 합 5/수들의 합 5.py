n = int(input())
cnt, start_idx, end_idx, sum = 1, 1, 1, 1

while end_idx != n:
    if sum == n:
        cnt += 1
        end_idx += 1
        sum += end_idx
    elif sum > n:
        sum -= start_idx
        start_idx += 1
    else:
        end_idx += 1
        sum += end_idx
    
print(cnt)