## general
def find_invalid(tickets: list[int], rules: dict):
    excluded = []
    to_remove = []
    for ticket in tickets:
        valid = True
        for number in ticket:
            tmp = False
            for rule in rules.values():
                for interval in rule:
                    tmp = tmp or (number >= interval[0] and number <= interval[1])

            if not tmp:
                excluded.append(number)
                valid = False

        if not valid:
            to_remove.append(ticket)

    for ticket in to_remove: tickets.remove(ticket)
    return excluded

## solution for the first half
def part1(tickets: list[int], rules: dict):
    res = 0
    for num in find_invalid(tickets.copy(), rules):
        res += num

    return res

## solution for the second half

# recursive backtracker to solve the system, not actually used
def backtracker(poss: list[tuple], done: dict, rule: int):
    if rule >= len(poss):
        return True
    else:
        i = 0
        while i < len(poss[rule][1]):
            if not poss[rule][1][i] in done.values():
                done[poss[rule][0]] = poss[rule][1][i]
                if aux2(poss, done, rule + 1):
                    return True
                else:
                    i = -1

            i += 1

        if poss[rule][0] in done.keys():
            done.pop(poss[rule][0])

        return False

# solves the sistem
def solve(poss: dict):
    res = {}
    for i in range(0, len(poss)):
        for key in poss.keys():
            if len(poss[key]) == 1:
                to_remove = poss[key][0]
                res[key] = to_remove
                for row in poss.values():
                    if len(row) > 0: row.remove(to_remove)

    return res

# returns a dict of conditions and rows that respect them
def possible_rows(tickets: list[int], rules: dict):
    res = {}
    for key, rule in rules.items():
        res[key] = []
        for i in range(0, len(tickets[0])):
            valid = True
            for ticket in tickets:
                tmp = False
                for interval in rule:
                    tmp = tmp or (ticket[i] >= interval[0] and ticket[i] <= interval[1])
                
                valid = valid and tmp

            if valid:
                res[key] = res[key] + [i]

    return res


def part2(tickets: list[int], rules: dict):
    tickets = tickets.copy()
    find_invalid(tickets, rules)
 
    poss = possible_rows(tickets, rules)
    order = solve(poss.copy())

    res = 1
    for key in order.keys():
        if key[:9] == 'departure':
            res *= tickets[0][order[key]]
    
    return res
    
## read input
def parse(line: str, tickets: list[int], rules: dict):
    if len(line) > 0: 
        if line[0].isdigit():
            tickets.append([int(n) for n in line.split(',')])
        else:
            split = line.split(':')
            if len(split[1]) > 0:
                numbers = [item.split('-') for item in split[1].split('or')]
                rules[split[0]]  = [(int(n[0]), int(n[1])) for n in numbers]

with open('input.txt', 'r') as input_file:
    tickets = []
    rules = {}
    for line in input_file.read().rstrip('\n').split('\n'): parse(line, tickets, rules)

## output answer 
print(part1(tickets, rules))
print(part2(tickets, rules))
