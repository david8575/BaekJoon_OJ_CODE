n = int(input())

user = []
for _ in range(n):
    age, name = map(str, input().split())
    user.append([int(age), name])

user = sorted(user, key=lambda x : x[0])

for i in range(n):
    print(f"{user[i][0]} {user[i][1]}")