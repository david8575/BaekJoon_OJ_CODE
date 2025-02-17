def recursion(s, l, r, count):
    count+=1
    if l >= r: 
        return 1, count
    elif s[l] != s[r]: 
        return 0, count
    else: 
        return recursion(s, l+1, r-1, count)

def isPalindrome(s, count):
    return recursion(s, 0, len(s)-1, count)

n = int(input())
for _ in range(n):
    word = input()
    count = 0
    answer = list(isPalindrome(word, count))
    print(answer[0], answer[1]) 
    