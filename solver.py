board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def solve(board):
    find = findEmpty(board)
    # if there are no empty squares the board is solved.
    if not find:
        return True
    #still empty squares, so the board is not solved.
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(board, i, (row, col)):

            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False

def valid(board, num, pos):
    #check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check col
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #check square
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY*3, boxY*3+3):
        for j in range(boxX*3, boxX*3+3):
            if board[i][j]==num and (i,j) != pos:
                return False
    return True

def printBoard(board): #just prints the board, duh
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                    print (board[i][j])
            else:
                    print(str(board[i][j]) + " ", end = "")

def findEmpty(board): #find an empty space on the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

printBoard(board)
print("\n")
solve(board)
printBoard(board)