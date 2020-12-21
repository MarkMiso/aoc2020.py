# imports
import numpy as np

## general code
def neighbours(dim, coords: tuple):
    res = []
    for i in range (-1, 2):
        for j in range (-1, 2):
            for k in range (-1, 2):
                z = coords[0] + i
                y = coords[1] + j
                x = coords[2] + k

                if not (z == coords[0] and y == coords[1] and x == coords[2]):
                    l = dim.shape
                    if (z >= 0 and z < l[0]) and (y >= 0 and y < l[1]) and (x >= 0 and x < l[2]):
                        res.append(dim[z][y][x])
                    else:
                        res.append(b'.')

    return res

def next_cycle(dim):
    nex_dim = np.chararray(tuple(size + 2 for size in dim.shape))
    nex_dim[:] = '.'
    l = dim.shape
    ln = nex_dim.shape

    for i in range(ln[0]):
        for j in range(ln[1]):
            for k in range(ln[2]):
                z = i - 1
                y = j - 1
                x = k - 1
                n = neighbours(dim, (z, y, x))
                actives = n.count(b'#')

                if (z >= 0 and z < l[0]) and (y >= 0 and y < l[1]) and (x >= 0 and x < l[2]):
                    cube = dim[z][y][x]
                else:
                    cube = b'.'

                if cube == b'#':
                    if(actives == 2 or actives == 3):
                        nex_dim[i][j][k] = b'#'
                    else:
                        nex_dim[i][j][k] = b'.'

                else:
                    if(actives == 3):
                        nex_dim[i][j][k] = b'#'
                    else:
                        nex_dim[i][j][k] = b'.'

    return nex_dim

def neighbours_4d(dim, coords: tuple):
    res = []
    for t in range (-1, 2):
        for i in range (-1, 2):
            for j in range (-1, 2):
                for k in range (-1, 2):
                    w = coords[0] + t
                    z = coords[1] + i
                    y = coords[2] + j
                    x = coords[3] + k

                    if not (w == coords[0] and z == coords[1] and y == coords[2] and x == coords[3]):
                        l = dim.shape
                        if (w >= 0 and w < l[0]) and (z >= 0 and z < l[1]) and (y >= 0 and y < l[2]) and (x >= 0 and x < l[3]):
                            res.append(dim[w][z][y][x])
                        else:
                            res.append(b'.')

    return res

def next_cycle_4d(dim):
    nex_dim = np.chararray(tuple(size + 2 for size in dim.shape))
    nex_dim[:] = '.'
    l = dim.shape
    ln = nex_dim.shape
    
    for t in range(ln[0]):
        for i in range(ln[1]):
            for j in range(ln[2]):
                for k in range(ln[3]):
                    w = t - 1
                    z = i - 1
                    y = j - 1
                    x = k - 1
                    n = neighbours_4d(dim, (w, z, y, x))
                    actives = n.count(b'#')

                    if (w >= 0 and w < l[0]) and (z >= 0 and z < l[1]) and (y >= 0 and y < l[2]) and (x >= 0 and x < l[3]):
                        cube = dim[w][z][y][x]
                    else:
                        cube = b'.'

                    if cube == b'#':
                        if(actives == 2 or actives == 3):
                            nex_dim[t][i][j][k] = b'#'
                        else:
                            nex_dim[t][i][j][k] = b'.'

                    else:
                        if(actives == 3):
                            nex_dim[t][i][j][k] = b'#'
                        else:
                            nex_dim[t][i][j][k] = b'.'

    return nex_dim

## solution for the first half
def part1(dimension):
    for i in range(0, 6):
        dimension = next_cycle(dimension)

    #print(dimension)
    return np.count_nonzero(dimension == b'#') 

## solution for the second half
def part2(dimension):
    for i in range(0, 6):
        dimension = next_cycle_4d(dimension)

    return np.count_nonzero(dimension == b'#') 

## read input
with open('input.txt', 'r') as input_file:
    slice = [line for line in input_file.read().rstrip('\n').split('\n')]

    dimension = np.chararray((1, 1, len(slice), len(slice[0])))
    dimension[:] = '.'

    for y in range(0, len(slice)):
        for x in range(0, len(slice[y])):
            dimension[0][0][y][x] = slice[y][x]

## output answer 
print(part1(dimension[0]))
print(part2(dimension))
