n = int(input())
for i in range(n):
    num, text = map(str, input().split())
    for j in range(len(text)):
        print(text[j]*int(num), end="")
    print()