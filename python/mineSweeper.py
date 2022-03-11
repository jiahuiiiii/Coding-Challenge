def mineSweeper():
    # take input from user ex. 3 4 5 means 3 rows, 4 colums, and 5 mines in the board
    input1 = input("Please enter the row count, column count and mine count of your board: ")

    # split the user input, convert each value into int and map them into 3 different variables
    splittedInput1 = input1.split() # ['3', '3', '2']
    rows, cols, mineCount = [int(i) for i in splittedInput1] # [3. 3. 2] rows = 3, cols = 3, mineCount = 2

    # initialize a 2D array filled with empty string with the height of "rows" and the width of "cols"
    mine = [["" for i in range(cols)] for i in range(rows)] # [['', '', ''], ['', '', ''], ['', '', '']]

    # take input mineCount times from the user and replace corresponding element in the board with "*"
    for i in range(mineCount):
        mineCoorsInput = input(f"Please enter the x and y coordinate of mine #{i}: ")
        mineRow, mineCol = [int(i) for i in mineCoorsInput.split()]
        mine[mineRow][mineCol] = '*' # [['', '', '*'], ['', '', '*'], ['', '', '']]

    # index of neighbours relatived to the element in board
    neighbour = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1]
    ]

    # loop through every single element in the board
    for i in range(rows):
        for j in range(cols):
            if mine[i][j] != '*':
                neighbourSUSCount = 0

                # loop through all neighbours of each element and check if they are SUS
                for n in range(len(neighbour)):
                    if (i+neighbour[n][0] >= 0 and i+neighbour[n][0] < rows):
                        if (j+neighbour[n][1] >= 0 and j+neighbour[n][1] < cols):
                            if (mine[i+neighbour[n][0]][j+neighbour[n][1]] == '*'):
                                neighbourSUSCount += 1

                # replace the element with the number of SUS neighbours
                mine[i][j] = str(neighbourSUSCount)

    # print the result
    print("\n".join("".join(i) for i in mine))
    return

    # aww yeah
mineSweeper()