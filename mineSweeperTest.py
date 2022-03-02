
from posixpath import split


def mine_sweeper():
    input1 = input('Enter the row count, column count and total number of mines in the minefield: ')
    rows, cols, mines = [int(i) for i in input1.split()]
    minefield = [["" for j in range(cols)] for i in range(rows)]

    for i in range(mines):
        mine_coors = input(f'Enter the coordinates of mine #{i}: ')
        mineRow, mineCols = [int(i) for i in mine_coors.split()]
        minefield[mineRow][mineCols] = '*'

    neighbours = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]

    for i in range(rows):
        for j in range(cols):
            if minefield[i][j] != '*':
                sus_neighbours = 0

                for n in range(len(neighbours)):
                    if (i + neighbours[n][0] >= 0) and (i + neighbours[n][0] < rows):
                        if (j + neighbours[n][1] >= 0) and (j + neighbours[n][1] < cols):
                            if minefield[i + neighbours[n][0]][j + neighbours[n][1]] == '*':
                                sus_neighbours += 1
                minefield[i][j] = str(sus_neighbours)
    
    print("\n".join("".join(i) for i in minefield))
    return

mine_sweeper()