n, q = map(int, input().split())
word = list(input())

for _ in range(q):
    order, src, des = map(int, input().split())
    src -= 1
    des -= 1

    if order == 1:
        cnt = 0
        for i in range(src, des):
            if word[i] != word[i+1]:
                cnt += 1

        print(cnt+1)
                
    if order == 2:
        for i in range(src, des+1):
            id = ord(word[i]) - ord('A')  
            id = (id + 1) % 26 
            word[i] = chr(id + ord('A'))
            