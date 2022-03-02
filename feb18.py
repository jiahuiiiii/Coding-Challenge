
def minesweeping_field():
    m = int(input('Enter the number of row: '))
    n = int(input('Enter the number of column '))
    z = int(input('Enter the number of mine: '))
    mine_coordinates = []
    i = 1
    while i <= z:
        mine_coordinates.append(input(f'Enter the coordinates of mine {i}: '))
        i += 1
    print(mine_coordinates)
    lst = [[0 for j in range(n)] for i in range(m)]
    for y, x in [[int(j) for j in i.split()] for i in mine_coordinates]:
        lst[y][x] = '*'
    
    for i in lst:
        for j in i:
            mine_around = 0
            if j != '*':
                if i.index(lst) != 0:
                    if lst[j-1][i.index(lst)-1] == '*':
                        mine_around += 1
                    if lst[j-1][i.index(lst)] == '*':
                        mine_around += 1
                    if lst[j-1][i.index(lst)+1] == '*':
                        mine_around += 1
                if j != 0:
                    if lst[j][i.index(lst)-1] == '*':
                        mine_around += 1
                if j != i[-1]:
                    if lst[j][i.index(lst)-1] == '*':
                        mine_around += 1
                if i != lst[-1]:
                    if lst[j+1][i.index(lst)-1] == '*':
                        mine_around += 1
                    if lst[j+1][i.index(lst)] == '*':
                        mine_around += 1
                    if lst[j+1][i.index(lst)+1] == '*':
                        mine_around += 1
                
                
    print(lst)
    # list_in_row = [list(i) for i in list(zip(*lst))]
    # print(list_in_row)
    # for i in list_in_row:
    #     for j in i:
    #         if j != '*':
    #             if i[j + 1] != 0 and i[j + 1] == '*':
    #                 mine_around += 1
    #             if i[j] != 0 and i[j - 1] == '*':
    #                 mine_around += 1
    #     if i != 0:
    #         for k in list_in_row[i - 1]:
            
print(minesweeping_field())