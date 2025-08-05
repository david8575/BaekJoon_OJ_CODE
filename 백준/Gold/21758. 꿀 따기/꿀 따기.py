n = int(input())
honey = list(map(int, input().split()))

p_honey = [0] * n
p_honey[0] = honey[0]
for i in range(1, n):
    p_honey[i] = p_honey[i - 1] + honey[i]

answer = 0

for i in range(1, n-1):
    bee_1 = p_honey[n-1] - honey[0] - honey[i]
    bee_2 = p_honey[n-1] - p_honey[i]
    answer = max(answer, bee_1 + bee_2)

for i in range(n-2, 0, -1):
    bee_1 = p_honey[n-1] - honey[n-1] - honey[i]
    bee_2 = p_honey[i-1]
    answer = max(answer, bee_1 + bee_2)

for i in range(1, n-1):
    bee_1 = p_honey[i] - honey[0]
    bee_2 = p_honey[n-2] - p_honey[i-1]
    answer = max(answer, bee_1 + bee_2)

print(answer)