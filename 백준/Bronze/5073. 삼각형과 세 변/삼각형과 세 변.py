while(True):
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and  c == 0:
        break
    else:
        list1 = []
        list1.append(a)
        list1.append(b)
        list1.append(c)
        list1.sort()
        if list1[2]>=list1[1]+list1[0]:
            print("Invalid")
        else:
            if a == b and a == c and b == c:
                print("Equilateral")
            elif a != b and a != c and b != c:
                print("Scalene")
            else:
                print("Isosceles")