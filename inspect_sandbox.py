from typing import get_type_hints


class Foo:
    herp: str
    baz: str

    def __init__(self):
        self.herp = ""
        self.baz = ""


class Bar:
    def __init__(self):
        self.foo = 0.123
        self.derp = 1


if __name__ == "__main__":
    print("Type hints for Foo class.")
    print(f"Getting type hints from object: {get_type_hints(Foo())}")
    print(f"Getting type hints from class: {get_type_hints(Foo)}")

    print("Type hints for Bar class.")
    b = Bar()
    print(f"Getting type hints from object: {get_type_hints(b)}")
    # print(f"Getting type hints from class: {get_type_hints(Bar)}")
