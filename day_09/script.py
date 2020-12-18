def valid(preamble: list[int], number: int):
    i = 0
    cond = False
    
    while (i < len(preamble) and not cond):
        j = i + 1
        while (j < len(preamble) and not cond):
            cond = number == (preamble[i] + preamble[j])
            j += 1
        i += 1

    return cond

def preamble_calc(numbers: list[int], index: int, lenght: int):
    return  numbers[:-(len(numbers) - index)][-lenght:]

## solution for the first half
def part1(numbers: list[int], preamble_len: int):
    not_valid = False
    i = preamble_len
    while (i < len(numbers) and not not_valid):
        preamble = (preamble_calc(numbers, i, preamble_len))
        if (not valid(preamble, numbers[i])):
            not_valid = numbers[i]
        i += 1

    return not_valid

## solution for the second half
def part2(numbers: list[int], invalid_number: int):
    i = 0
    shortcut = False
    while (i < len(numbers) and not shortcut):
        j = i + 1
        count = numbers[i]
        i += 1
        while (j < len(numbers) and count < invalid_number):
            count += numbers[j]
            j += 1

        if (count == invalid_number):
            shortcut = True

    num_set = preamble_calc(numbers, j, j - (i - 1))
    return max(num_set) + min(num_set)

## read input
with open('input.txt', 'r') as input_file:
    numbers = [int(line) for line in input_file.read().rstrip('\n').split('\n')]

## output answer 
invalid_number = part1(numbers, 25)
print(invalid_number)
print(part2(numbers, invalid_number))
