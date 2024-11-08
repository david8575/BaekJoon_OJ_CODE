from itertools import combinations
 
L, C = map(int,input().split())
alphabets = input().split()
alphabets.sort()

for combination in combinations(alphabets, L):
    sum1 = combination.count('a') + combination.count('e') +combination.count('i') + combination.count('o') + combination.count('u')
    sum2 = L - sum1
    if sum1 >= 1 and sum2 >= 2:
        ans = ""
        for c in combination:
            ans += c
        print(ans)