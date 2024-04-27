from dataclasses import dataclass, field
from pprint import pprint


@dataclass
class A:
    num1: int
    num2: int
    float1: float
    something: str = field(default="")


class B:
    def __init__(self, num1: int, num2: int, float1: float, something=""):
        self.num1 = num1
        self.num2 = num2
        self.float1 = float1
        self.something = something


a = A(1, 2, 123.0)
b = B(1, 2, 123.2)

dir_a = dir(a)
dir_b = dir(b)

pprint(f"{dir(a)=}")
pprint(f"{dir(b)}")

unique = list(set(dir_a).symmetric_difference(set(dir_b)))
pprint(unique)
