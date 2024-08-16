from pprint import pprint


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
