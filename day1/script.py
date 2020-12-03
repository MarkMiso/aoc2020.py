def part1(data):
    input_lenght = len(data)
    cond = False
    i = 0
    while ((i <  input_lenght) and (not cond)):
        cond = (2020 - data[i]) in data
        i += 1
        
    return (data[i - 1]) * (2020 - data[i - 1])

def part2(data):
    input_lenght = len(data)
    cond = False
    i = 0
    while ((i <  input_lenght) and (not cond)):
        j = i + 1
        while ((j <  input_lenght) and (not cond)):
            k = j + 1
            while ((k <  input_lenght) and (not cond)):
                cond = (data[i] + data[j] + data[k]) == 2020
                k += 1
            j += 1
        i += 1

    return (data[i - 1] * data[j - 1] * data[k - 1])

data = []
with open('input.txt', 'r') as file_input:
    for line in file_input:
        data.append(int(line))


print(part2(data))
