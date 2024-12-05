word = input()

num_k = 0
num_r = 0
for i in range(len(word)):
    if (word[i] == 'K'):
        num_k += 1
    if (word[i] == 'R'):
        num_r += 1

start = -1
end = len(word)
max_len = 0

for i in range(num_k // 2 + 1):
    if num_r == 0:
        break
    
    max_len = max(max_len, 2*i+num_r)
    start += 1
    end -= 1
    
    while start < end and word[start] != 'K':
        start += 1
        num_r -= 1
    while start < end and word[end] != 'K':
        end -=1
        num_r -= 1
        
print(max_len)