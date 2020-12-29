# base  = 3
# side  = base*base
#
# # pattern for a baseline valid solution
# def pattern(r,c): return (base*(r%base)+r//base+c)%side
#
# # randomize rows, columns and numbers (of valid base pattern)
# from random import sample
# def shuffle(s): return sample(s,len(s))
# rBase = range(base)
# rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
# cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
# nums  = shuffle(range(1,base*base+1))
#
# # produce board using randomized baseline pattern
# board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
# squares = side*side
# empties = squares * 3//4
# for p in sample(range(squares),empties):
#     board[p//side][p%side] = 0
#

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def solve(bo):
    find=find_empty(bo)
    if not find:
        return True
    else:
        row,col=find

    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i

            if solve(bo):
                return True
            else:
                bo[row][col]=0
    return False






def valid(bo,num,pos):
    # Check That Row (For Each Column) whether another same number is already present or not
    for i in range(9):
        if i!=pos[1]:
            if bo[pos[0]][i]==num:
                return False

    # Check That Column (For Each Row) whether another same number is already present or not
    for i in range(9):
        if i!=pos[0]:
            if bo[i][pos[1]]==num:
                return False

    #Check 3x3 cube in which the number is present whether another same number is already present in that cube or not
    #Check small boxes
    #box represented as
    #[0,0] [0,1] [0,2]
    #[1,0] [1,1] [1,2]
    #[2,0] [2,1] [2,2]
    #where box_y,box_x are box coordinates which helps us categorize which box we are in

    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False

    return True





def print_board(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print("-----------------------")
        for j in range(9):
            if j % 3==0 and j != 0:
                print(" | ",end="")
            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+" ",end="")

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j]==0:
                return (i,j)  # row,col
    return None

print_board(board)
print()
solve(board)
print()
print_board(board)