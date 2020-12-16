## solution for the first half
def p1_aux(bags: dict, rules: list):
    if (rules[0][0] == 0):
        return False
    else:
        cond = False
        i = 0
        while (i < len(rules)):
            rule = rules[i]
            i += 1
            if (rule[1] == 'shiny gold' or cond):
                return True
            else:
                cond = p1_aux(bags, bags[rule[1]])

        return cond

def part1(rules: dict):
    count = 0
    res = False
    for bag, rule in rules.items():
        if (rule[0][0] != 0 and bag != 'shiny gold'):
            count += p1_aux(rules, rule)

    return count

## solution for the second half
def p2_aux(bags: dict, rules: list):
    if (rules[0][0] == 0):
        return 0
    else:
        count = 0
        for rule in rules:
            count += rule[0] + rule[0] * p2_aux(bags, bags[rule[1]])

        return count

def part2(rules: dict):
    return p2_aux(rules, rules['shiny gold'])

## read input
def parse(line: str, d: dict):
    fields = [content.replace('.', ' ').replace('bags', '').replace('bag', '').replace('no other', '').strip() for content in line.split('contain')]
    d[fields[0]] = [(int('0' + ''.join(filter(str.isdigit, c))), c.replace(''.join(filter(str.isdigit, c)), '').strip()) for c in fields[1].split(',')]
    return 0

with open('input.txt', 'r') as input_file:
    rules = {}
    for line in input_file.read().rstrip('\n').split('\n'):
        parse(line, rules)

## output answer 
print(part1(rules))
print(part2(rules))
