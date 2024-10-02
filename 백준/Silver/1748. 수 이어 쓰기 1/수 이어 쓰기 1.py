n = int(input())

answer = 0
digit = 1
start = 1

while start <= n:
    end = min(n, start * 10-1)
    answer += (end-start+1) * digit
    digit += 1
    start *= 10

print(answer)
