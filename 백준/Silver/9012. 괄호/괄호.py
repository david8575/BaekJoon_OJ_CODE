n = int(input())

for i in range(n):
    str = input()
    count = 0
    check = 0
    for j in range(len(str)):
        if (str[j] == "("):
            count += 1
        if (str[j] == ")"):
            count -= 1
            if (count < 0):
                check+=1
    if (check == 0):
        if (count == 0):
            print("YES")
        else:
            print("NO")
    else:
            print("NO")