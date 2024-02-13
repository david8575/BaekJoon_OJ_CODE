test = int(input())
for i in range(test):
    h, w, n = map(int, input().split())
    row = (n % h)*100
    col = ((n // h)+1)
    if row == 0:
        row = h*100
        col -= 1
    print(row+col)
