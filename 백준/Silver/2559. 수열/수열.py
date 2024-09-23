n, k = map(int, input().split())
temperature = list(map(int, input().split()))

psum = [0] * n
psum[0] = temperature[0]

for i in range(1, n):
    psum[i] = temperature[i] + psum[i-1] 

diff_temp = []
for i in range(n-k+1):
    if i == 0:
        sum = psum[i+k-1]
    else:
        sum = psum[i+k-1] - psum[i-1]     
    diff_temp.append(sum)  
print(max(diff_temp))