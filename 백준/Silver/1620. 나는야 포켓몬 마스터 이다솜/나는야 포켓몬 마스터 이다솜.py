import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_to_number = dict() 
number_to_pokemon = dict()  

for num in range(1, n + 1):
    name = input().strip()
    pokemon_to_number[name] = num
    number_to_pokemon[num] = name


for _ in range(m):
    problem = input().strip()

    if problem.isdigit():
        problem = int(problem)
        print(number_to_pokemon[problem])
    else: 
        print(pokemon_to_number[problem])
