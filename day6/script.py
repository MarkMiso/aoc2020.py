## solution for the first half
def part1(groups: list):
    count = 0
    for group in groups:
        no_dups = ''.join(set(group[1]))
        count += len(no_dups)

    return count

## solution for the second half
def part2(groups: list):
    count = 0
    for group in groups:
        no_dups = ''.join(set(group[1]))
        for letter in no_dups:
            count += group[0] == group[1].count(letter)

    return count

## read input
def parse(line: str):
    return (line[:-1].count('\n') + 1, line.replace('\n', ''))

with open('input.txt', 'r') as input_file:
    groups = [parse(line) for line in input_file.read().split('\n\n')]

## output answer 
print(part1(groups))
print(part2(groups))
