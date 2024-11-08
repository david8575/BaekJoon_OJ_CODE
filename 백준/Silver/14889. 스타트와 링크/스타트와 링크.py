from itertools import combinations

n = int(input())
aby = []

for i in range(n):
    temp = list(map(int, input().split()))
    aby.append(temp)

players = [(i) for i in range(n)]

min_diff = 100
for combination in combinations(players, n//2):
    team_1 = combination
    team_2 = []
    for player in players:
        if player not in team_1:
            team_2.append(player)
    
    
    
    power_1 = 0
    power_2 = 0
    
    for i in team_1:
        for j in team_1:
            power_1 += aby[i][j]
            
    for i in team_2:
        for j in team_2:
            power_2 += aby[i][j]

    if min_diff > abs(power_1 - power_2):
        min_diff = abs(power_1 - power_2)

print(min_diff)
# 1 1 2 3 5 5 = 17 / 2 2 3 4 5 5 = 19