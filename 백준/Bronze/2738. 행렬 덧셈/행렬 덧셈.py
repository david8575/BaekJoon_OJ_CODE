n, m = map(int,input().split())
matrix1 = [[0]*m for _ in range(n)]
matrix2 = [[0]*m for _ in range(n)]

for i in range(n):
    matrix1[i] = list(map(int, input().split()))
for i in range(n):
    matrix2[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(matrix1[i][j]+matrix2[i][j], end=" ")
    print()