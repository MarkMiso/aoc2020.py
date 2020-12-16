## imports
import math

## solution for the first half
def wait_list(time:int, busses: list):
    wait = []
    i = 0

    for bus in busses:
        wait.append(-time)
        while (wait[i] < 0):
            wait[i] += bus

        i += 1

    return wait

def part1(time: int, busses: list[str]):
    wait = wait_list(time, busses)
    return min(wait) * busses[wait.index(min(wait))]

## solution for the second half

# bruteforce method to calculate the result, not actually used
def bruteforce(busses: list[int], indexes: list[int]):
    max_n = max(busses)
    max_i = indexes[busses.index(max_n)]

    res = max_n
    cond = False
    while (not cond):
        cond = True
        i = 0
        while(cond and i < len(busses)):
            cond = cond and ((res - max_i + indexes[i])%busses[i] == 0)
            i += 1

        res += max_n

    return (res - max_n) - max_i

# given a number returns it's list of prime factors
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            if (not d in primfac): primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

# finds gdc using extended euclidian algorithm
def gcd_extended(a, b):  
    if a == 0 :   
        return b, 0, 1
             
    gcd, x1, y1 = gcd_extended(b%a, a)  
     
    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd, x, y 

# solves a congurance
def congruence_compute(a: int, b: int, m: int):
    a = a%m
    b = b%m
    gcd = gcd_extended(a, m)
    return int(b*gcd[1]/gcd[0])%m, m

    
# calculates the result of the system
def CRT_compute(reminders: list[int], divisors: list[int]):
    elements = list(set([(reminders[i], prime) for i in range(0, len(divisors)) for prime in primes(divisors[i])]))
    ele = [ele[1] for ele in elements]

    n = []
    for i in range(1, len(ele)):
        n.append(math.prod(ele[:(i-1)] + ele[i:]))
    n.append(math.prod(ele[:-1]))
    
    y = [congruence_compute(n[i], 1, elements[i][1]) for i in range(0, len(n))]
    res = 0
    for i in range(0, len(y)):
        res += elements[i][0] * n[i] * y[i][0]

    return res % math.prod(ele)

def part2(busses: list[int], indexes: list[int]):
    return CRT_compute([-x for x in indexes], busses)

## read input
with open('input.txt', 'r') as input_file:
    input_lines = input_file.read().split('\n')
    timestamp = int(input_lines[0])
    elements = input_lines[1].split(',')
    indexes = [i for i in range(0, len(elements)) if elements[i].isdigit()]
    busses = [int(bus) for bus in elements if bus.isdigit()]

## output answer 
print(part1(timestamp, busses))
print(part2(busses, indexes))
