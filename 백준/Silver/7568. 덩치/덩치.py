n = int(input())
people = []
for _ in range(n):
    person = list(map(int, input().split()))
    people.append(person)

rank = [1] * n
for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for i in range(n):
    print(rank[i], end = " ")