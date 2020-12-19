## imports

## solution for both halfs 
def play(numbers: list[int], iterations: int):
    nums = {}
    i = 0
    for num in numbers:
        nums[num] = i
        i += 1
    
    spoken = 0
    for i in range(len(numbers), iterations - 1):
        if (spoken in nums):
            old = spoken
            spoken = (i - nums[spoken])
            nums[old] = i
        else:
            nums[spoken] = i
            spoken = 0

    return spoken

## read input
with open('input.txt', 'r') as input_file:
    numbers = [int(n) for n in input_file.read().rstrip('\n').split(',')]

## print results
print(play(numbers, 2020))
print(play(numbers, 30000000))
