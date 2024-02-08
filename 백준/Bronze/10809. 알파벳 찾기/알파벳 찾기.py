str = input()
index_list = [-1]*26

for i in range(26):
    pos = 0
    check = 0
    for j in range(len(str)):
        if chr(97+i) == str[j]:
            if check == 0:
                index_list[i] = pos
                check+=1
        else:
            pos+=1
for i in index_list:
    print(i, end=" ")