"""Take a string, make it a spongebob meme string."""

import random

import typer


def main(sentence: str):
    choices = [0, 0, 0, 1, 1, 2, 3, 4]

    i = 2
    res_str = sentence[0].lower()
    res_str += sentence[1].upper()

    while i <= len(sentence) - 1:
        ch = random.choice(choices)
        if (next_i := i + ch) > len(sentence) - 1:
            break
        print("start\n", f"span this many string indices: {ch}")

        slice_str = (
            sentence[i:next_i] + sentence[next_i].upper() if sentence[next_i] else ""
        )
        print(f"string slice: {slice_str}")
        res_str += slice_str
        i = next_i if next_i else i + 1
        print(f"next index start: {i}", "\nend\n")

    print(f"Spongebob'd string: {res_str}")


if __name__ == "__main__":
    typer.run(main)
