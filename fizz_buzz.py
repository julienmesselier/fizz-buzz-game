def fizz_buzz():
    """Function which builds a list filled with numbers from 1 to 100
    But:
    Multiples of 3 are replaced by Fizz
    Multiples of 5 are replaced by Buzz
    Multiples of 3 and 5 are replaced by FizzBuzz
    Numbers are stored as strings
    """
    def evaluate(n):
        if not n % 3 and not n % 5:
            return 'FizzBuzz'
        if not n % 3:
            return 'Fizz'
        if not n % 5:
            return 'Buzz'
        return str(n)

    return [evaluate(n) for n in range(1, 101)]


def fizz_buzz_variation_1():
    """Same result as fizz_buzz with a variation in the implementation
    One liner using list comprehension, string slicing
    and property of "or" which returns the first valid operand
    """
    return ["Fizz"[i % 3 * 4:] + "Buzz"[i % 5 * 4:] or str(i) for i in range(1, 101)]

# fizz_buzz_2 variation: cycles
from itertools import cycle, count, islice


def fizz_buzz_variation_2():
    """Another variation. Using:
    - cycle infinite iterator. cycle('ABCD') --> A B C D A B C D ...
    - count infinite iterator. count(10) --> 10 11 12 13 ...
    - islice iterator. islice('ABCDEF', 2) --> A B
    """
    fizzes = cycle([""] * 2 + ["Fizz"])
    buzzes = cycle([""] * 4 + ["Buzz"])
    both = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    fizzbuzz = (word or str(number) for (word, number) in zip(both, count(1)))
    return [i for i in islice(fizzbuzz, 100)]

# fizz_buzz_3 variation: numpy

import numpy as np


def fizz_buzz_variation_3():
    """Another variation using conditions / choices list from numpy"""
    x = np.arange(1, 101)
    condition_list = [(x % 3 == 0) & (x % 5 == 0), x % 3 == 0, x % 5 == 0, x]
    choice_list = ["FizzBuzz", "Fizz", "Buzz", x]
    return list(np.select(condition_list, choice_list))

# Next : 4th variation using machine learning and keras?