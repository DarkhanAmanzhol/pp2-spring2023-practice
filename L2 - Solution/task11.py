number: int = int(input('number: '))

for i in range(1, number + 1):
    message: str = ''
    if i % 15 == 0:
        message = 'FizzBuzz'
    elif i % 3 == 0:
        message = 'Fizz'
    elif i % 5 == 0:
        message = 'Buzz'
    else:
        message = i

    print(f' '*(8 - len(str(message))), end=f'{message}')
    print(',' if i != number else '.', end=' ')

    if i % 10 == 0:
        print()