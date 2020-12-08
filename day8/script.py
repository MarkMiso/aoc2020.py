def execute(instruction: tuple, index: int, value: int):
    if (instruction[0] == 'nop'):
        return (index + 1, value)
    elif (instruction[0] == 'acc'):
        return (index + 1, value + instruction[1])
    elif (instruction[0] == 'jmp'):
        return (index + instruction[1], value)

## solution for the first half
def part1(code: list):
    i = 0
    acc = 0
    executed = []
    while(i < len(code) and not i in executed):
        res = execute(code[i], i, acc)
        executed.append(i)
        i = res[0]
        acc = res[1]

    return  acc

## solution for the second half
def brute_force(code: list):
    i = 0
    acc = 0
    cond = False
    executed = []
    while(i < len(code) and not cond):
        cond = i in executed
        if (not cond):
            res = execute(code[i], i, acc)
            executed.append(i)
            i = res[0]
            acc = res[1]

    return not cond

def part2(code: list):
    i = 0
    shortcut = False
    while(i < len(code) and not shortcut):
        new_code = code.copy()

        if (code[i][0] == 'jmp'):
            new_code[i] = ('nop', code[i][1])
        elif (code[i][0] == 'nop'):
            new_code[i] = ('jmp', code[i][1])

        shortcut = brute_force(new_code)
        i += 1

    return part1(new_code)

## read input
def parse(line: str):
    elem = line.split(' ')
    return (elem[0],int(elem[1]))

with open('input.txt', 'r') as input_file:
    code = [parse(line) for line in input_file.read().rstrip('\n').split('\n')]

## output answer 
print(part1(code))
print(part2(code))
