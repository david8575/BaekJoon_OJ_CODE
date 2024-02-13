n = int(input())
for i in range(n):
    ans = input()
    score = 0
    cons = 0
    for j in range(len(ans)):
        if ans[j] == "O":
            score += (cons+1)
            cons += 1
        elif ans[j] == "X":
            cons = 0
    print(score)