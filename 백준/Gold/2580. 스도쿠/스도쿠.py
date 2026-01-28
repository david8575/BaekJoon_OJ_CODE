def is_valid(row, col, num):
    if num in sudoku[row]:
        return False
    
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    box_row = (row//3) * 3
    box_col = (col//3) * 3

    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col+3):
            if num == sudoku[i][j]:
                return False
            
    return True

def solve():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(i, j, num):
                        sudoku[i][j] = num

                        if solve():
                            return True
                        
                        sudoku[i][j] = 0

                return False
            
    return True

sudoku = [list(map(int, input().split(" "))) for _ in range(9)]
# print(sudoku)
# print("=================")
solve()
for row in sudoku:
    print(*row)
