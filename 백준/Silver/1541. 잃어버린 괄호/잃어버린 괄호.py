answer = 0
a = list(map(str, input().split("-")))

def my_sum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(a)):
    temp = my_sum(a[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)