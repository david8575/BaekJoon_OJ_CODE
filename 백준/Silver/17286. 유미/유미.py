from itertools import permutations

x = []
y = []

for _ in range(4):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b) 

min_move = 10000000
for p in permutations([1,2,3], 3):
    pos_x = x[0]
    pos_y = y[0]

    move = 0
    for i in p:
        move += (abs(pos_x - x[i]) ** 2 + abs(pos_y - y[i]) ** 2) ** 0.5
        pos_x = x[i]
        pos_y = y[i]
    
    min_move = min(move, min_move)

print(int(min_move))