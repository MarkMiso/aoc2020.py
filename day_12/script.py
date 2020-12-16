# imports
import math

## general code
def rotate(pivot: list, subject: list, deg: int):
    coords = ['N', 'E', 'S', 'W']
    pivot[0] = coords[int((coords.index(pivot[0]) - deg/90)%4)]

    newx = (subject[0] * math.cos(math.radians(deg))) - (subject[1] * math.sin(math.radians(deg)))
    newy = (subject[0] * math.sin(math.radians(deg))) + (subject[1] * math.cos(math.radians(deg)))

    subject[0] = int(round(newx))
    subject[1] = int(round(newy))


def eval(boat: list, way: list, instruction: tuple):
    if (instruction[0] == 'N'):
        way[1] += instruction[1]

    elif (instruction[0] == 'S'):
        way[1] -= instruction[1]

    elif (instruction[0] == 'E'):
        way[0] += instruction[1]

    elif (instruction[0] == 'W'):
        way[0] -= instruction[1]

    elif (instruction[0] == 'L'):
        rotate(boat, way, instruction[1])

    elif (instruction[0] == 'R'):
        rotate(boat, way, -instruction[1])

    elif (instruction[0] == 'F'):
        boat[1] += way[0]*instruction[1]
        boat[2] += way[1]*instruction[1]

## solution for the first half
def part1(boat: list, instructions: list[tuple]):
    way = [0, 0]
    for instruction in instructions:
        if (instruction[0] == 'F'):
            if (boat[0] == 'N'):
                way[1] = 1

            elif (boat[0] == 'S'):
                way[1] = -1

            elif (boat[0] == 'E'):
                way[0] = 1

            elif (boat[0] == 'W'):
                way[0] = -1

            eval(boat, way, instruction)
        else:
            eval(boat, way, instruction)
            boat[1] += way[0]
            boat[2] += way[1]

        way[0] = 0
        way[1] = 0

    return abs(boat[1]) + abs(boat[2])

## solution for the second half
def part2(boat: list, way: list, instructions):
    for instruction in instructions:
        eval(boat, way, instruction)

    return abs(boat[1]) + abs(boat[2])

## read input
def parse(instruction: str):
    return (instruction[:1], int(instruction[1:]))

with open('input.txt', 'r') as input_file:
    instructions = [parse(line) for line in input_file.read().rstrip('\n').split('\n')]
    boat = ['E', 0, 0]
    waypoint = [10, 1]

## output answer 
print(part1(boat.copy(), instructions))
print(part2(boat.copy(), waypoint.copy(), instructions))
