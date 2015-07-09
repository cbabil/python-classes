'''
generator.py uses timeit() to show the difference between
a list comprehension and the list() function applied to:
    - a list of a million random numbers.
    - a generator that generates a sequence of a million random numbers.
'''

from random import sample
from timeit import Timer


def rand_gen():
    '''
    Generates a random number
    from a list of one million
    random numbers
    '''
    rand_lst = sample(range(1000000), 1000000)
    for i in rand_lst:
        yield i


if __name__ == "__main__":

    rand_lst_timer_comprehension = Timer(
        "[num for num in sample(range(1000000), 1000000)]", "from __main__ import sample")
    print("random list time (list comprehension):",
          rand_lst_timer_comprehension.timeit(number=10))

    rand_lst_timer_function = Timer(
        "list(num for num in sample(range(1000000), 1000000))", "from __main__ import sample")
    print("random list time (list function):",
          rand_lst_timer_function.timeit(number=10))

    rand_gen_timer_comprehension = Timer(
        "[num for num in rand_gen()]", "from __main__ import rand_gen")
    print("random gen time (list comprehension):",
          rand_gen_timer_comprehension.timeit(number=10))

    rand_gen_timer_function = Timer(
        "list(num for num in rand_gen())", "from __main__ import rand_gen")
    print("random gen time (list function):",
          rand_gen_timer_function.timeit(number=10))