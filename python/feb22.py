# y = y0 + ((y1 - y0)/(x1 - x0)) * (x - x0)
def linear_interpolation():
    input1 = input('Please enter the number of inputs: ')
    lst = [input(f'Please enter the value of input # {i+1}: ') for i in range(int(input1))]
    print(lst)
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    for i, v in enumerate(lst):
        if v == "#": # if the value of the current index is #
            # copy the current index to a new value
            j = i - 1 # minus one to let the loop start from the left side of the '#' but not the '#' itself
            while j >= 0: # while the index is bigger than 0 and the element isn't '#'
                if lst[j] != '#':
                    x0 = j + 1 # set x0 as j + 1 as indicies are zero-based
                    y0 = int(lst[j]) # set y0 as the corresponding value of j, but not j + 1
                    break # stop the loop
                j -= 1 # j minus one as we want to loop from the current index to the beginning of the array until we find a calculatable number
                # because sometimes there might be two or more '#' next to each other
            
            j = i + 1 # j plus one still because of want it to start after the '#'
            while j < len(lst): # while j is smaller than the length of list and not equal to '#'
                if lst[j] != '#':
                    x1 = j + 1 # x1 equalto j + 1 as indicies are zero-based, but we dont want it
                    y1 = int(lst[j]) # set y1 to the corresponding value of x1
                    break # stop the loop once the program finish all of this
                j += 1 # j + 1 as we want to continue looping to the end of the list until we find a calculatable value
            ans = y0 + ((y1 - y0) / (x1 - x0)) * (i + 1 - x0) # the fucking equation that i dont't fucking understand
            print(x0, y0, x1, y1) # just cheking, not necessary lol
            print("{:.2f}".format(ans)) # round the result to two decimal places and print it

linear_interpolation()