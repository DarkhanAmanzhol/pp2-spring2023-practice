def get_arithmetic_operation(operator):
    if operator == '+':
        return lambda x, y: x + y
    elif operator == '-':
        return lambda x, y: x - y
    elif operator == '*':
        return lambda x, y: x * y
    elif operator == '/':
        return lambda x, y: x / y
    else:
        print(f'Invalid arithmetic operator `{operator}`.')

def get_conditional_operation(operator):
    if operator == '>':
        return lambda x, y: x > y
    elif operator == '<':
        return lambda x, y: x < y
    elif operator == '>=':
        return lambda x, y: x >= y
    elif operator == '<=':
        return lambda x, y: x <= y
    else:
        print(f'Invalid conditional operator `{operator}`.')


a = [1,2,3,4,5]
result = []

command, args = input().split(' ', 1)

if command in ['map', 'filter']:
    operator, operand = args.split(' ', 1)
    operand = int(operand)

    for elem_i in a:

        if command == 'map':
            result.append(get_arithmetic_operation(operator)(elem_i, operand))

        elif command == 'filter':
            if get_conditional_operation(operator)(elem_i, operand):
                result.append(elem_i)

elif command in ['progression', 'fold']:
    operator = args

    operation = get_arithmetic_operation(operator)

    result.append(a[0])

    for elem_i in a[1:]:

        if command == 'progression':
            result.append(operation(result[-1], elem_i))

        elif command == 'fold':
            result[0] = operation(result[0], elem_i)

print(result)