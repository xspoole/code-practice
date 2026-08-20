import random, time, copy

WIDTH = 60
HEIGHT = 20

# create a list of lists for the cells
next_cells = [] # empty list
for x in range(WIDTH):
    column = [] # create columns for the length of WIDTH
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') # 'living' cell

        else:
            column.append(' ') # 'dead' cell
    next_cells.append(column)

# main program loop
while True:
    print('\n\n\n\n\n') # \n is for newlines
    current_cells = copy.deepcopy(next_cells) # make a copy of next_cells list of lists

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end = '') # print the # or a space
        print() # print a newline at the end of the row

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left_coord = (x - 1) % WIDTH # % WIDTH ensures left_coord is always between 0 and WIDTH - 1
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # count number of living neighbors
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1 # top-left neighbor is alive
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1
            if current_cells[x][below_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1
            
            # set cell based on Conway's Game of Life Rules (I have no idea how this game works ngl)
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] == '#'
            else:
                next_cells[x][y] = ' '
        
        time.sleep(1)
