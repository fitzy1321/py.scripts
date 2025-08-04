"""Take a string, make it a spongebob meme string."""

import random

import typer


def main(sentence: str):
    choices = [0, 1, 1, 2, 3, 4]

    sentence_list = list(sentence)

    sentence_list[0] = sentence_list[0].lower()
    sentence_list[1] = sentence_list[1].upper()
    i = 2

    while i <= len(sentence) - 1:
        ch = random.choice(choices)
        next_index = i + ch if ch else i + 1
        if next_index > len(sentence) - 1:
            break
        print("start\n", f"span this many string indices: {ch}")
        sentence_list[next_index] = sentence_list[next_index].upper()

        i = next_index
        print(f"next index start: {i}", "\nend\n")

    sb_sentence = "".join(sentence_list)
    print(f"Spongebob'd string: {sb_sentence}")


if __name__ == "__main__":
    typer.run(main)
