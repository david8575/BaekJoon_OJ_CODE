str = input()
ans = ""

for i in range(len(str)):
    if str[i].isupper():
        ans += str[i].lower()
    else:
        ans += str[i].upper()

print(ans)