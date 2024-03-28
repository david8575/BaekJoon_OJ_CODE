def checkBigNum(a,b):
    if a>b: print("Yes")
    else: print("No")

while(True):
    a,b = map(int, input().split())
    if a == 0 and b == 0: break
    checkBigNum(a,b)