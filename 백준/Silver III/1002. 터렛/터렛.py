n = int(input())

for i in range(n):
    x1,y1,z1,x2,y2,z2 = map(int, input().split())

    distance1 = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) 
    distance2 = (z2-z1)*(z2-z1)
    distance3 = (z2+z1)*(z2+z1)
    
    if distance1 == 0 and distance2 == 0:
        print(-1)
    else:
        if distance1 > distance3:
            print(0)
        elif distance1 < distance2:
            print(0)
        elif distance1 == distance2:
            print(1)
        elif distance1 == distance3:
            print(1)
        else:
            print(2)