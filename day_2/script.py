def count_occurrences(letter, string):
    count = 0
    for l in string:
        count += letter == l

    return count

def part1(range, letter, password):
    l = 0
    p = 0
    r = 0
    res = 0

    for i in letter:
        count = count_occurrences(letter[l], password[p])
        res += (count >= range[r][0] and count <= range[r][1])
        l += 1
        p += 1
        r += 1

    return res

def part2(range, letter, password):
    l = 0
    p = 0
    r = 0
    res = 0

    for r in range:
        pos1 = r[0] - 1
        pos2 = r[1] - 1
        cond1 = (letter[l] == password[p][pos1] and letter[l] != password[p][pos2])
        cond2 = (letter[l] != password[p][pos1] and letter[l] == password[p][pos2])
        res += cond1 or cond2
        l += 1
        p += 1

    return res
        
range = []
letter = []
password = []

with open('input.txt', 'r') as input_file:
    input_line = input_file.readlines()
    for line in input_line:
        number = line.split()
        range.append((int(number[0].split('-')[0]), int(number[0].split('-')[1])))
        letter.append(number[1].replace(':', ''))
        password.append(number[2])


print(part1(range, letter, password))
print(part2(range, letter, password))
