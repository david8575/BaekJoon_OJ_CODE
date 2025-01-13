n, m = map(int, input().split())

word = []
for _ in range(n):
    word.append(input())

count = 0
for _ in range(m):
    w = input()
    if w in word:
        count+=1 

print(count)