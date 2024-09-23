n, k ,b = map(int, input().split())

signal = [0] * n
for _ in range(b):
    signal[int(input())-1] = 1
    
psum = [0] * n
psum[0] = signal[0]
for i in range(1, n):
    psum[i] = psum[i-1] + signal[i]

repair = []
for i in range(n-k+1):
    if i == 0:
        sum = psum[i+k-1]
    else:
        sum = psum[i+k-1] - psum[i-1]
    repair.append(sum)

print(min(repair))
    