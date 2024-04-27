from functools import lru_cache

# Using tool to cache function values


@lru_cache(maxsize=1000)
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("n needs to be a positive int.")
    if n < 0:
        raise ValueError("n needs to be a postive int.")

    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for n in range(0, 101):
        print(f"{n}: {fibonacci(n)}")
