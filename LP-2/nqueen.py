# # N = 8
# # def is_safe(board,row,col):

# #     for i in range(col):
# #         if board[row][i]==1:
# #             return False
        
# #     for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
# #         if board[i][j] == 1:
# #             return False
    
# #     for i,j in zip(range(row,N,1), range(col,-1,-1)):
# #         if board[i][j] == 1:
# #             return False
        
# #     return True


# # def util(board, col):
# #     if col>=N:
# #         return True
    
# #     for i in range(N):
# #         if is_safe(board,i,col):
# #             board[i][col] = 1

# #             if util(board,col+1) == True:
# #                 return True
            
# #             board[i][col]=0

# #     return False

# # board = [[0 for i in range(N)]for i in range(N)]

# # util(board,0)

# # print(board)

# N = 8

# def is_safe(board,row,col):
    
#     for i in range(col):
#         if board[row][i]==1:
#             return False
        
#     for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
#         if board[i][j]==1:
#             return False
    
#     for i,j in zip(range(row,N,1), range(col,-1,-1)):
#         if board[i][j]==1:
#             return False
        
#     return True

# def util(board, col, no_of_queen, min_):

#     if col == N:
#         if no_of_queen < min_:
#             min_ = no_of_queen
#             return True
#         else:
#             return False
    
#     for i in range(N):
#         if is_safe(board, i, col):
#             board[i][col] = 1
#             if util(board, col+1, no_of_queen+1,min_):
#                 return True
            
#             board[i][col] = 0

#     return False

# board = [[0 for i in range(N)] for i in range(N)]
# min_=float('inf')
# util(board,0,0,min_)
# print(min_)
# for i in board:
#     print(i)


N = 8

def is_safe(board, row, col):
    # Check if there is a queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    return True

def solve_n_queens(board, col, queens_placed, min_cost):
    if col == N:
        if queens_placed < min_cost[0]:
            min_cost[0] = queens_placed
            return True
        else:
            return False
    
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, queens_placed + 1, min_cost):
                return True
            board[i][col] = 0

    return False

def n_queens():
    board = [[0] * N for _ in range(N)]
    min_cost = [float('inf')]  # Initialize with a large value
    solve_n_queens(board, 0, 0, min_cost)

    if min_cost[0] == float('inf'):
        print("No solution exists.")
    else:
        print("Minimum number of queens required to solve the N-Queens problem:", min_cost[0])
        print(board)

n_queens()
