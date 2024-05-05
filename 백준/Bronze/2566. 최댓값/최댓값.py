maxNum = -1
maxRow = -1
maxCol = -1
for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(9):
        if maxNum < arr[j]:
            maxNum = arr[j]
            maxRow = i
            maxCol = j


print(f"{maxNum}")
print(f"{maxRow+1} {maxCol+1}")