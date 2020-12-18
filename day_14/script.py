## imports
import re
import itertools

## solution for the first half
def part1(mem: list[tuple]):
    res = 0
    for n in mem:
        res += n[1]
    return res

## solution for the second half
def floating_eval(val: str, computed: list[tuple]):
    xs = [i for i, v in enumerate(val) if v[0] == 'X']
    base = ['0'] * len(xs)
    if (len(base) in [item[0] for item in computed]):
        perms = [item[1] for item in computed if item[0] == len(base)][0]
    else:
        permi = [tuple(base.copy())]
        for i in range(0, len(base)):
            base[i] = '1'
            permi += list(itertools.permutations(base))

        perms = list(set(permi)) 
        computed.append((len(base), perms))

    res = []
    for perm in perms:
        list_val = list(val)
        for ind in range(0, len(perm)):
            list_val[xs[ind]] = perm[ind]

        res.append(int(''.join(list_val), 2))

    return res

## read input
def apply_mask(val: int, mask: str):
    val = str(bin(val))[2:]
    for i in range(len(mask) - 1, -1, -1):
        if (mask[i] != 'X'):
            ind = len(val) - (len(mask) - i)
            if (ind < 0):
                val = ('0' * (-ind)) + val
                ind = 0

            val = val[:ind] + mask[i] + val[ind+1:]

    return int(val, 2)

def apply_mask_V2(val: int, mask: str):
    val = str(bin(val))[2:]
    for i in range(len(mask) - 1, -1, -1):
        if (mask[i] != '0'):
            ind = len(val) - (len(mask) - i)
            if (ind < 0):
                val = ('0' * (-ind)) + val
                ind = 0

            val = val[:ind] + mask[i] + val[ind+1:]
    
    return val

def decode(line: list[str], masks: list[str], mem: list[tuple], version: int, computed: list[tuple]):
    if (line.startswith('mask')):
        masks.append(line[7:])

    else:
        r = re.compile(r"mem\[(\d+)\] = (\d+)")
        match = r.match(line).groups()
        occurrences = [i for i, v in enumerate(mem) if v[0] == match[0]]
        if (len(occurrences) > 0):
            for i in occurrences: mem.pop(i)

        if (version == 1):
            val = int(match[1])
            mem.append((match[0], apply_mask(val, masks[-1])))
        elif (version == 2):
            val = apply_mask_V2(int(match[0]), masks[-1])
            for ind in floating_eval(val, computed):
                occurrences = [i for i, v in enumerate(mem) if v[0] == ind]
                if (len(occurrences) > 0):
                    for i in occurrences: mem.pop(i)

                mem.append((ind, int(match[1])))

with open('input.txt', 'r') as input_file:
    input_lines = input_file.read().rstrip('\n').split('\n')

    masks = []
    mem = []
    computed = []
    for line in input_lines: decode(line, masks, mem, 1, computed)
    print(part1(mem))

    masks.clear()
    mem.clear()
    for line in input_lines: decode(line, masks, mem, 2, computed)
    print(part1(mem))
