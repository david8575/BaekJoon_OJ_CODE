while True:
    try:
        s, t = map(str, input().split())

        pos = 0
        check = True
        for i in range(len(s)):
            while pos < len (t) and t[pos] != s[i]:
                pos += 1
                
            if pos < len(t):
                pos += 1
            else:
                check = False
                break
        if check:
            print("Yes")
        else:
            print("No")            
    except:
        break