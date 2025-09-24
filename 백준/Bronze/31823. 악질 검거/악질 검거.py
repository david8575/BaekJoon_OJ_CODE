n, m = map(int, input().split())

team_record = {}

for _ in range(n):

    record = list(map(str, input().split()))
    name = record[-1]
    record.pop()

    max = 0
    cnt = 0
    for i in record:
        if i == ".":
            cnt+=1

            if cnt > max:
                max = cnt
        else:
            cnt = 0

    team_record[name] = max

print(len(set(team_record.values())))
for key in team_record:
    print(team_record[key], key)