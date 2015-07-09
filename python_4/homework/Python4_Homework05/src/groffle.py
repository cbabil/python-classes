"""
Program for optimization. Python 4, Lesson 5.

Calculates the groffle speed of a knurl widget
of average density given by user input.
"""

from math import log
from timeit import Timer


def groffle_slow(mass, density):
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density)
        total += masslog / (i + 1)

    return total


def groffle_fast(mass, density):
    return sum([(log(mass * density)) / i for i in range(1, 10001)])


def groffle_faster(mass, density):
    return sum(map((log(mass * density)).__truediv__, range(1, 10001)))

mass = 2.5
density = 12.0

if __name__ == "__main__":

    "Compare executing time"
    timer = Timer("total = groffle_slow(mass, density)",
                  "from __main__ import groffle_slow, mass, density")
    print("[groffle_slow] time:", timer.timeit(number=1000),
          " result:", groffle_slow(mass, density))
    timer = Timer("total = groffle_fast(mass, density)",
                  "from __main__ import groffle_fast, mass, density")
    print("[groffle_fast] time:", timer.timeit(number=1000),
          " result:", groffle_fast(mass, density))

    timer = Timer("total = groffle_faster(mass, density)",
                  "from __main__ import groffle_faster, mass, density")
    print("[groffle_faster] time:", timer.timeit(number=1000),
          " result:", groffle_faster(mass, density))

    "Check answers"
    print("Result error: ")
    print("Difference between fast and slow: ", abs(
        groffle_fast(mass, density) - groffle_slow(mass, density)))
    print("Difference between faster and slow: ", abs(
        groffle_faster(mass, density) - groffle_slow(mass, density)))

    import cProfile as profile
    print('-' * 100)
    print('SLOW')
    print('-' * 100)
    profile.run('groffle_slow(mass, density)')

    print('-' * 100)
    print('FAST')
    print('-' * 100)
    profile.run('groffle_fast(mass, density)')

    print('-' * 100)
    print('FASTER')
    print('-' * 100)
    profile.run('groffle_faster(mass, density)')
