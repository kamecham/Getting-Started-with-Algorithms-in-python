"2.6 Fibonacci Series"
"一度計算した値をメモ化することで実行速度が上がる"

memo = {1:1, 2:1}

def fibonacci(number):
    " the value of the Fibonacci sequence."
    if number in memo:
        return memo[number]
    memo[number] = fibonacci(number - 2) + fibonacci(number - 1)
    return memo[number]


print(fibonacci(10))
