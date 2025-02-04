import sys
input = sys.stdin.readline

n = int(input())
gom = set()
count = 0

for _ in range(n):
    user = input().strip()
    if user == "ENTER":
        count += len(gom)
        gom = set()
    else:
        gom.add(user)

count += len(gom)
print(count)