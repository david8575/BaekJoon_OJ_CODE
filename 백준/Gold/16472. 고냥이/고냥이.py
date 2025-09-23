n = int(input())
word = input()

start, end = 0,0
cnt = [0]*26
cnt[ord(word[0])-97]+=1
ans = 0
num_cnt = 1

while start < len(word) and end < len(word):
    if num_cnt <= n:
        ans = max(ans, end-start+1)
        end += 1

        if end < len(word):
            cnt[ord(word[end])-97] += 1

            if cnt[ord(word[end])-97] == 1:
                num_cnt += 1

    else:
        start += 1
        cnt[ord(word[start-1])-97]-=1

        if cnt[ord(word[start-1])-97] == 0:
            num_cnt -= 1
print(ans)