"""Find the lowest, postive integer not present in a list of numbers

Ignore 0 or negative numbers
"""


def solution(nums: list[int]) -> int:
    if len(nums) == 0:
        return 1

    for i in range(1, len(nums) + 1):
        if i not in nums:
            return i
    # if everything found, return -1
    return -1


if __name__ == "__main__":
    assert solution([]) == 1
    assert solution([1, 2, 3, 4, 5]) == -1
    assert solution([6, 9, 2, 0, 1]) == 3, "Your solution didn't work!"
