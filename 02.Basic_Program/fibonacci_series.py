"2.6 Fibonacci Series"

def fibonacci(number):
    " the value of the Fibonacci sequence."

    if number in (1, 2):
        return 1
    return fibonacci(number - 2) + fibonacci(number - 1)


print(fibonacci(10))
