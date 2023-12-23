from random import randint
import random
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

# board=[
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0],
#     ]

# board=[
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

val=0
def random_numbers(board): 
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column]==0:
                for num in random.sample(range(0,9), 9):
                    if is_valid(row,column,num):
                        board[row][column]=num
                        if solve():
                            return True
                        board[row][column]=0
                return False
    return True

def grid_maker(board):
    val=0
    for row in range(len(board)):
        for column in range(len(board)):
            val=randint(0,2)
            if val==0 or val==1:
                board[row][column]=0
            else:
                continue
    return board

def print_board():
    global board
    for i in range(len(board)):
        if i%3==0:
            print("-------------------------")
        for j in range(len(board)):
            if j%3==0:
                print("|",end = " ")
            print(board[i][j],end=" ")
            if j==8:
                print("|",end="")
        print()
    print("-------------------------")

def is_valid(x,y,n):
    global board
    for i in range(9):
        if board[i][y]==n:
            return False
    for j in range(9):
        if board[x][j]==n:
            return False
    x_position=(x//3)*3
    y_position=(y//3)*3
    for i in range(3):
        for j in range(3):
            if board[x_position+i][y_position+j]==n:
                return False
    return True

def solve():
    global board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==0:
                for k in range(1,10):
                    if is_valid(i,j,k):
                        board[i][j]=k
                        solve()
                        board[i][j]=0
                return 
    print_board()
    input("More?")

# random_numbers(board)
print_board()
board=grid_maker(board)
print_board()
# solve()
