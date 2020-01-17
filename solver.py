__author__ = "Joystick"

def solve(bo):
    """
    Solves a sudoku board using backtracking
    :param bo: 2d list of ints
    :return: solution
    """
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    """
    Returns if the attempted move is valid
    :param bo: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(bo):
    """
    finds an empty space in the board
    :param bo: partially complete board
    :return: (int, int) row col
    """

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None

def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")