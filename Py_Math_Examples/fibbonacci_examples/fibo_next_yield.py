input_data_range = int(input('Your number range: '))

def fib_gen():
    a = 0
    b = 1

    while True:
        yield b
        b = a + b
        a = b - a

for value in fib_gen():
    if value > input_data_range:
        break
    print(value, end = ' ')
