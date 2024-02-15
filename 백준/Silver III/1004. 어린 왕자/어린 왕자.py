test = int(input())

for i in range(test):
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    count = 0
    for j in range(n):
        x3, y3, r = map(int, input().split())
        if (x3-x1)**2+(y3-y1)**2 < r**2:
            if (x3-x2)**2+(y3-y2)**2 > r**2:
                count+=1
        elif (x3-x1)**2+(y3-y1)**2 > r**2:
            if (x3-x2)**2+(y3-y2)**2 < r**2:
                count+=1
    print(count)