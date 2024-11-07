import typing

_T_co = typing.TypeVar("_T_co", covariant=True)

# Python's Strings are kinda weird.
# They're technically Sequences of Strings
# So `str is Sequence[str]`
# That's a problem for some scenarios.
# What if you really wanted a generic container of strings, but exclude accidently 'fatfinger'
# str as a Sequence typing?

# This Protocol kinda works, basically, it type checks for container types and against str types
# by forcing a specific constaint on one of the dunder methods? I think?

# Anyway, mypy and other type checkers will see the error, but the code will still execute.
# So grain of 🧂


class SeqMinusStr(typing.Protocol[_T_co]):
    """
    if a Protocol would define the interface of Sequence, this protocol
    would NOT allow str/bytes as their __contains__ is incompatible with the definition in Sequence.
    methods from: https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection
    """

    def __contains__(self, value: object, /) -> bool:
        raise NotImplementedError

    def __getitem__(self, index, /):
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __iter__(self) -> typing.Iterator[_T_co]:
        raise NotImplementedError

    def __reversed__(self, /) -> typing.Iterator[_T_co]:
        raise NotImplementedError


def join_strs(things: SeqMinusStr[str]):
    derp = ""
    for it in things:
        derp += " " + it
    return derp


print(join_strs(("testing", "testing", "testing")))
print(join_strs(["is", "this", "thing", "on?"]))

# this line will show a type error, but will still run in python interpreter
# print(join_strs("this should not pass!"))
