from pprint import pprint
from typing import Any


def deep_equal(a: Any, b: Any) -> bool:
    """Recusively compare 'basic' python types and containers for equality ✊."""
    if type(a) is not type(b):
        return False
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return False
        return all(deep_equal(a[k], b[k]) for k in a)
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(deep_equal(x, y) for x, y in zip(a, b))
    return a == b


def main():  # noqa
    a: dict = {
        "some": "value",
        "a_bool": True,
        "this": "is",
        "a_str": "this is a string",
    }
    b: dict = {
        "a_str": "different string, yo",
        "a_bool": False,
        "b": 123123,
        "c": 125551,
    }
    c: dict = {"asdasd": "Fasdfas", "ywekjf": "129sdhdf"}

    z = a | b | c
    pprint(z)


if __name__ == "__main__":
    main()
