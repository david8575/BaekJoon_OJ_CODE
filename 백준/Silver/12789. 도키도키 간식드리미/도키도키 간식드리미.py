n = int(input())

students = list(map(int, input().split()))

stack = []

cur = 1

for sutdent in students:
    stack.append(sutdent)

    while stack and stack[-1] == cur:
        stack.pop()
        cur += 1

if stack:
    print("Sad")
else:
    print("Nice")