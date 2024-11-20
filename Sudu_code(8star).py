#solving sudu_code by 8star algorithm

grid = [[0,0,0,0,0,0,6,8,0],
        [0,0,0,0,7,3,0,0,9],
        [3,0,9,0,0,0,0,4,5],
        [4,9,0,0,0,0,0,0,0],
        [8,0,3,0,5,0,9,0,2],
        [0,0,0,0,0,0,0,3,6],
        [9,6,0,0,0,0,3,0,8],
        [7,0,0,6,8,0,0,0,0],
        [0,2,8,0,0,0,0,0,0]]       
def valid_moves(grid,row,col,no):
    if no in grid[row]:
        return False
    for x in range(9):
        if grid[x][col]==no:
            return False
    top_left_row=row-(row%3)
    top_lef_col=col-(col%3)
    for i in range(3):
        for j in range(3):
            if grid[top_left_row+i][top_lef_col+j]==no:
                return False
    return True
def solvig(grid,row,col):
    if col==9:
        if row==8:
            return True
        else:
            row+=1
            col=0
    if grid[row][col]>0:
        return solvig(grid,row,col+1)
    for i in range(1,10):
        if valid_moves(grid,row,col,i):
            grid[row][col]=i
            if solvig(grid,row,col+1):
                return True
        grid[row][col]=0
    return False
            
            
if solvig(grid,0,0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print("\n")
else:
        print(" no solution found for this suduco")