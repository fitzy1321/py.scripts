def decorator(func):
    def wrapper(*args, **kwargs):
        print('In Decorator: ')
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@decorator
def print_message(msg):
    print(msg)


@decorator
def fib(n):
    if n in [0, 1, 2]:
        return n
    return fib(n - 1) + fib(n - 2)


print_message('Hello from Python!')

print([fib(n) for n in range(20)])
