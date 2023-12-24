# def permutation(nums,current_list):
#     if len(nums)==len(current_list):
#         print(current_list)
#         return
#     for num in nums:
#         if num not in current_list:
#             current_list.append(num)
#             permutation(nums,current_list)
#             current_list.pop()
# list1=[2,3,4]
# permutation(list1,[])


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def custom_board():
    board=[]
    for i in range(9):
        row=list(map(int,input(f"Enter the values for the row {i}: ").split()))
        board.append(row)
        print(board)
        if not is_valid_board(board):
            print("Invalid board as there is a repeating value")
            print_board(board)
            break

def is_valid_board(board):
    for row in range(9):
        for column in range(9):
            if board[row][column]!=0:
                if not is_valid(row,column,board[row][column]):
                    return False
    return True


def print_board(board):
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



def is_valid(row,column,n):
    global board
    for i in range(9):
        if board[i][column]==n:
            print(f"{n}")
            return False
    for j in range(9):
        if board[row][j]==n:
            print(f"{n}")
            return False
    x_position=(row//3)*3
    y_position=(column//3)*3
    for i in range(3):
        for j in range(3):
            if board[x_position+i][y_position+j]==n:
                print(f"{n}")
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
# board=random_numbers(board)
custom_board()
# print_board(board)
# if solve():
#     print("Solved")
#     print_board(board)
# else:
#     print("Not solvable")