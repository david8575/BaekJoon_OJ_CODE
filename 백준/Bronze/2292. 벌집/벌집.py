num = int(input())
level = 1
cnt = 1
while(num > level):
    level += 6 * cnt
    cnt+=1
print(cnt)