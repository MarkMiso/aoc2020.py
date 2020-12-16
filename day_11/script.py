# prevent intdex out of range
def illegal(seat: tuple, w: int, h: int):
    row = seat[0]
    col = seat[1]
    return row < 0 or col < 0 or row > h or col > w


def predict(seats: list[list], row: int, col: int, tolerance: int, rules: int):
    if (rules == 1):
        check_list = gen_list_p1(row, col, len(seats[0]) - 1, len(seats) - 1)
    elif (rules == 2):
        check_list = gen_list_p2(seats, row, col, len(seats[0]) - 1, len(seats) - 1)

    occupied = 0
    for seat in check_list:
        occupied += seats[seat[0]][seat[1]] == '#'

    if (seats[row][col] == 'L' and occupied == 0):
        res = '#'
    else:
        if (seats[row][col] == '#' and occupied >= tolerance):
            res = 'L'
        else:
            res = seats[row][col]

    return res

def stabilize(seats: list[list], tolerance: int, rules: int):
    stabilized = False
    while (not stabilized):
        layout = []
        for row in seats:
            layout.append(row.copy())

        for i in range (0, len(seats)):
            for j in range (0, len(seats[i])):
                layout[i][j] = predict(seats, i, j, tolerance, rules)

        stabilized = layout == seats
        seats = layout

    return layout

## solution for the first half
def gen_list_p1(row :int, col: int, w: int, h: int):
    seats = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            seats.append((row + i, col +j))

    seats.remove((row, col))
    for seat  in seats.copy():
        if illegal(seat, w, h):
            seats.remove(seat)
    
    return seats

def part1(seats: list[list]):
    count = 0
    for ele in stabilize(seats, 4, 1):
        count += ele.count('#')

    return count

## solution for the second half
def gen_list_p2(l: list, row :int, col: int, w: int, h: int):
    seats = []

    i = row + 1
    while (not illegal((i, col), w, h) and l[i][col] == '.'):
        i += 1
    seats.append((i, col))

    i = row - 1
    while (not illegal((i, col), w, h) and l[i][col] == '.'):
        i -= 1
    seats.append((i, col))
    
    j = col + 1
    while (not illegal((row, j), w, h) and l[row][j] == '.'):
        j += 1
    seats.append((row, j))

    j = col - 1
    while (not illegal((row, j), w, h) and l[row][j] == '.'):
        j -= 1
    seats.append((row, j))

    i = row + 1
    j = col + 1
    while (not illegal((i, j), w, h) and l[i][j] == '.'):
        i += 1
        j += 1
    seats.append((i, j))

    i = row - 1
    j = col + 1
    while (not illegal((i, j), w, h) and l[i][j] == '.'):
        i -= 1
        j += 1
    seats.append((i, j))

    i = row - 1
    j = col - 1
    while (not illegal((i, j), w, h) and l[i][j] == '.'):
        i -= 1
        j -= 1
    seats.append((i, j))

    i = row + 1
    j = col - 1
    while (not illegal((i, j), w, h) and l[i][j] == '.'):
        i += 1
        j -= 1
    seats.append((i, j))

    #seats.remove((row, col))
    for seat  in seats.copy():
        if illegal(seat, w, h):
            seats.remove(seat)
    
    return seats

def part2():
    count = 0
    for ele in stabilize(seats, 5, 2):
        count += ele.count('#')

    return count

## read input
with open('input.txt', 'r') as input_file:
    seats = [list(line) for line in input_file.read().rstrip('\n').split('\n')]

## output answer 
print(part1(seats))
print(part2())