# imports
import numpy as np

## solution of the first half
def part1(passports, necessary):
    number = len(necessary)
    valid = 0
    for passport in passports:
        match = 0
        for entry in passport:
            match += entry[0] in necessary

        valid += match == number
    
    return valid

## solution fo the second half
def part2(passports, necessary):
    lenght = len(necessary)
    valid = 0
    for passport in passports:
        match = 0
        for entry in passport:
            if (entry[0] in necessary):
                if (entry[0] == 'byr'):
                    number = int(entry[1])
                    match += number >= 1920 and number <= 2002

                elif (entry[0] == 'iyr'):
                    number = int(entry[1])
                    match += number >= 2010 and number <= 2020

                elif (entry[0] == 'eyr'):
                    number = int(entry[1])
                    match += number >= 2020 and number <= 2030

                elif (entry[0] == 'hgt'):
                    unit = entry[1][-2:]

                    if (unit == 'in'):
                        number = int(entry[1][:-2])
                        match += number >= 59 and number <= 76
                    elif (unit == 'cm'):
                        number = int(entry[1][:-2])
                        match += number >= 150 and number <= 193

                elif (entry[0] == 'hcl'):
                    tmp = 0
                    if (entry[1][0] == '#'):
                        for char in entry[1][1:]:
                            tmp += char in '0123456789abcdef'
                    
                    match += tmp == 6

                elif (entry[0] == 'ecl'):
                    match += entry[1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

                elif (entry[0] == 'pid'):
                    if (len(entry[1]) == 9):
                        tmp = True
                        try:
                            int(entry[1])
                        except:
                            tmp = False
                        
                        match += tmp
        
        valid += match == lenght
    
    return valid

## read input
passports = []
with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()

    entry = []
    for line in input_lines:
        strings = line.split()
        for string in strings:
            couple = string.split(':')
            entry.append((couple[0], couple[1]))

        if (not strings):
            passports.append(tuple(entry))
            entry = []

    passports.append(tuple(entry))

necessary = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',]

## output answer 
print(part1(passports, necessary))
print(part2(passports, necessary))
