from itertools import combinations

n, m = map(int, input().split())

answers = combinations(range(1, n+1),m)
for answer in answers:
    for i in range(len(answer)):
        print(answer[i], end=" ")
        
    print()