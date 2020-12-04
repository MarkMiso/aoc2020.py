def t_gen(tile, row, col):
    return tile[row][col % len(terrain[0])]

## solution of the first half
def part1(terrain, slope):
    row = 0
    col = 0
    trees = 0

    while (row < len(terrain)):
        trees += t_gen(terrain, row, col) == '#'
        row += slope[1]
        col += slope[0]

    return trees

## solution fo the second half
def part2(terrain, slopes):
    res = 1
    for slope in slopes:
        res *= part1(terrain, slope)

    return res

## read input
terrain = []
with open('input.txt', 'r') as input_file:
    input_line = input_file.readlines()
    for line in input_line:
        terrain.append(line[:-1])

## output answer 
print(part1(terrain, (3, 1)))
print(part2(terrain, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
