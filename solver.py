board = [
    [0,0,0,9,5,7,8,2,1],
    [2,1,5,3,8,0,0,0,0],
    [7,0,9,4,0,0,3,6,5],
    [9,7,0,0,0,0,0,5,8],
    [8,0,0,6,9,5,0,0,7],
    [0,5,1,8,0,0,2,9,0],
    [1,6,0,5,4,0,0,0,0],
    [4,0,7,2,0,0,0,0,6],
    [5,2,0,0,0,8,0,4,0]
]

# * Displays the current configuration of the Board 
def display_board(board):
    print("")
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")

            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("")

