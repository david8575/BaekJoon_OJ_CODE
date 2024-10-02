poli = input()
answer = ""
count = 0
impossible = False
for i in range(len(poli)):
    if poli[i] == "X":
        count+=1
        if count == 4:
            answer+="AAAA"
            count = 0
    else:
        if count == 0:
            answer+="."
        elif count == 1:
            impossible = True
            break
        elif count == 2:
            answer+="BB"
            count = 0
            answer+="."
        elif count == 3:
            impossible = True
            break
if count == 1:
    impossible = True
elif count == 2:
    answer+="BB"
elif count == 3:
    impossible = True
    
if not impossible:
    print(answer)
else:
    print(-1)