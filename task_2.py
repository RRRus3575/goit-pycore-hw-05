import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text, func: Callable):
    numbers = func(text)

    sum_profit = sum(numbers)
    return sum_profit

print(sum_profit(text, generator_numbers))

