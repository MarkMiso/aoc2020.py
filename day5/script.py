## imports
import math

## auxiliary
def decode(seat):
    row = [0, 127]
    col = [0, 7]
    for letter in seat:
        if (letter == 'F'):
            row[1] = math.floor(((row[1] - row[0]) / 2) + row[0])

        elif (letter == 'B'):
            row[0] = math.ceil(((row[1] - row[0]) / 2) + row[0])

        elif (letter == 'L'):
            col[1] = math.floor(((col[1] - col[0]) / 2) + col[0])

        elif (letter == 'R'):
            col[0] = math.ceil(((col[1] - col[0]) / 2) + col[0])

    return (row[0], col[0])

def list_id(seats):
    ids = []
    for seat in seats:
        coord = decode(seat)
        ids.append((coord[0] * 8) + coord[1])

    return ids

## solution of the first half
def part1(seats):
    id = list_id(seats)
    return max(id)

## solution fo the second half
def part2(seats):
    id = list_id(seats)
    id.sort()

    cond = 0
    i = 0
    while (id[i] and not cond):
        cond = (id[i + 1]) and (id[i] + 2 == id[i + 1])
        i += 1

    return (id[i] - 1)

## read input
seats = []
with open('input.txt', 'r') as input_file:
    input_line = input_file.readlines()
    for line in input_line:
        seats.append(line[:-1])

## output answer 
print(part1(seats))
print(part2(seats))
