## solution for the first half
def part1(adapters: list[int]):
    full_adapters = sorted([0] + adapters + [max(adapters) + 3])

    i = 1
    joltage_in = 0
    joltage_differences = []
    while (i < len(full_adapters)):
        joltage_differences.append(full_adapters[i] - joltage_in)
        joltage_in = full_adapters[i]
        i += 1

    return (joltage_differences.count(1) * joltage_differences.count(3))

## solution for the second half
def calc(func):
    def wrapper(adapters: list[int], i: int, calculated: list):
        j = 0
        is_in = False
        while (j < len(calculated) and not is_in):
            is_in = i == calculated[j][0]
            j += 1
        
        if (is_in):
            res = calculated[j - 1][1]
        else:
            res = func(adapters, i, calculated)
            calculated.append((i, res))

        return res
    return wrapper

@calc
def aux_p2(adapters: list[int], i: int, calculated: list):
    if (i >= len(adapters) - 1):
        return 1
    else:
        res = 0
        j = i + 1
        while (j < len(adapters) and adapters[j] - adapters[i] <= 3):
            res += aux_p2(adapters, j, calculated)
            j += 1

        return res

def part2(adapters: list[int]):
    full_adapters = sorted([0] + adapters + [max(adapters) + 3])
    return aux_p2(full_adapters, 0, [])

## read input
with open('input.txt', 'r') as input_file:
    adapters = [int(line) for line in input_file.read().rstrip('\n').split('\n')]

## output answer 
print(part1(adapters))
print(part2(adapters))
