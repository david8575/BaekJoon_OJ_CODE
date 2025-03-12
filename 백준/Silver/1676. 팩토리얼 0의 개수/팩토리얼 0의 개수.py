n = int(input())
result = 1
for i in range(1, n+1):
    result *= i

result = list(str(result))

answer = 0
for i in range(len(result)-1, -1, -1):
    if int(result[i]) != 0:
        print(answer)
        break
    else:
        answer+=1