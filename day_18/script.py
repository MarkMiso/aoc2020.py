# imports

## general code
def evaluate(expression: str):
    last = 0
    operator = '+'
    i = 0
    while i < len(expression):
        element = expression[i]
        if element.isdigit():
            element = int(element)
            if operator == '+':
                last += element
            else:
                last *= element
        else:
            if element == '+' or element == '*':
                operator = element
            elif element == '(':
                res = evaluate(expression[(i + 1):])
                if operator == '+':
                    last += res[0]
                else:
                    last *= res[0]

                i += res[1] + 1

            elif element == ')':
                return last, i

        i += 1

    return last, i

## solution for the first half
def part1(expressions: list[str]):
    res = 0
    for expression in expressions:
        res += evaluate(expression)[0]
    
    return res

## solution for the second half
def evaluate_with_precedence(expression: str):
    last = 0
    operator = '+'
    i = 0
    multiplication = []
    while i < len(expression):
        element = expression[i]
        if element.isdigit():
            element = int(element)
            if operator == '+':
                last += element
            else:
                multiplication.append(last)
                last = element
        else:
            if element == '+' or element == '*':
                operator = element
            elif element == '(':
                res = evaluate_with_precedence(expression[(i + 1):])
                if operator == '+':
                    last += res[0]
                else:
                    multiplication.append(last)
                    last = res[0]

                i += res[1] + 1

            elif element == ')':
                b = last
                for ele in multiplication:
                    b *= ele

                return b, i

        i += 1

    b = last
    for ele in multiplication:
        b *= ele

    return b, i

def part2(expressions: list[str]):
    res = 0
    for expression in expressions:
        res += evaluate_with_precedence(expression)[0]
    
    return res

## read input
with open('input.txt', 'r') as input_file:
    expressions = [line.replace(' ', '') for line in input_file.read().rstrip('\n').split('\n')]

## output answer 
print(part1(expressions))
print(part2(expressions))
