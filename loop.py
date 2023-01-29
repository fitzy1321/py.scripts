"""Fun looping stuff from mCoding."""

# Video Source: https://www.youtube.com/watch?v=Qgevy75co8c

import timeit


def while_loop(n=100_000_000):
    """While loop is the slowest looping operation."""
    (i, s) = (0, 0)
    while i < n:
        s += i
        i += 1
    print(s)
    return s


def for_loop(n=100_000_000):
    """For loop is faster than while loop, but we can still do better."""
    s = 0
    for i in range(n):
        print(1)
        s += i
    print(s)
    return s


def for_loop_with_incr(n=100_000_000):
    """Adding redundent increment operation to for loop,
    to demonstrate why while loopis slow."""
    s = 0
    for i in range(n):
        s += i
        i += 1  # redundent increment
    return s


def for_loop_with_test(n=100_000_000):
    """Demonstrate while loop test, show why while loop is slow."""
    s = 0
    for i in range(n):
        if i < n:
            pass  # redundent test
        s += i
    return s


def for_loop_with_incr_and_test(n=100_000_000):
    """Not as bad as while looop (because of iterators),
    but still worse than standard for loop."""
    s = 0
    for i in range(n):
        if i < n:
            pass
        s += i
        i += 1
    return s


def sum_range(n=100_000_000):
    """Builtin operations will most likely be faster than looping."""
    s = sum(range(n))
    print(s)
    return s


# There was also a numpy example, but I didn't feel like installing numpy
# numpy wil usually be faster than builtin methods, because numpy is
# primarily written in C.


# use 'Sum of N natural numbers' equation (can't find the name)
def math_sum(n=100_000_000):
    """The Fastest operation is to use math equations."""
    s = (n * (n - 1)) // 2
    print(s)
    return s


def main():
    """Main executable of script."""
    print("while loop\t\t", timeit.timeit(while_loop, number=1))
    print("for pure\t\t", timeit.timeit(for_loop, number=1))
    # print("for increment\t\t", timeit.timeit(for_loop_with_incr, number=1))
    # print("for test\t\t", timeit.timeit(for_loop_with_test, number=1))
    # print("for increment and test\t", timeit.timeit(for_loop_with_incr_and_test,
    # number=1))
    print("sum range\t\t", timeit.timeit(sum_range, number=1))
    print("pure math\t\t", timeit.timeit(math_sum, number=1))


if __name__ == "__main__":
    main()
