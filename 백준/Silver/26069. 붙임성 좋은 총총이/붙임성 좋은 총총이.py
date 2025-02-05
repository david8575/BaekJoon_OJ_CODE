import sys
input = sys.stdin.readline

n = int(input())
dance = {'ChongChong'}

for _ in range(n):
    person1, person2 = input().split()

    if person1 in dance:
        dance.add(person2)
    
    if person2 in dance:
        dance.add(person1)

print(len(dance))