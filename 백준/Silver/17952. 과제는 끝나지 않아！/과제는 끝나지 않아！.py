n = int(input())

assignments = []
total = 0
for _ in range(n):
    info = list(map(int, input().split()))

    if info[0] == 0:
        if len(assignments) != 0:
            score, time = assignments.pop()

            if time == 1:
                total += score

            else:
                assignments.append((score, time-1))

    if info[0] == 1:
        score = info[1]
        time = info[2]
        if time == 1:
            total += score
        else:
            assignments.append((score, time-1)) 

print(total)