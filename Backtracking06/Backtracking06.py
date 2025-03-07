#BackJoon Algorithm NO.2580
#Backtracking

def row(a,n):
    for i in range(9):
        if n == sudoku[a][i]:
            return False
    return True