# Print this pattern
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********

# Base is 11, 6 rows
# height * 2 - 1


def print_stars(height: int) -> None:
    max_width = height * 2 - 1
    for i in range(1, height + 1):
        print(f"{i}   " + ("*" * (i * 2 - 1)).center(max_width))


def main() -> None:
    print_stars(6)


if __name__ == "__main__":
    raise SystemExit(main())
