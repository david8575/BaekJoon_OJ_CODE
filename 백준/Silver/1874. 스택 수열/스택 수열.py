import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * n

for i in range(n):
    nums[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    seq = nums[i]
    if seq >= num:
        while seq >= num:
            stack.append(num)
            num+=1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        m = stack.pop()
        if seq < m:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)