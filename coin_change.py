# from functools import lru_cache
from collections import defaultdict


def _min_no_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def min_num_of_coins(target: int, coins: set[int]):
    if not hasattr(min_num_of_coins, "memo"):
        min_num_of_coins.memo = {}

    try:
        return min_num_of_coins.memo[target]
    except KeyError:
        pass

    if target == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            sub = target - coin
            if sub < 0:
                continue
            answer = _min_no_none(answer, min_num_of_coins(sub, coins) + 1)  # type: ignore

    min_num_of_coins.memo[target] = answer
    return answer


# @lru_cache
# def min_coins_memoized(target: int, coins: set[int]):
#     answer = 0
#     if target == 0:
#         return answer
#     else:
#         for coin in coins:
#             sub = target - coin
#             if sub < 0:
#                 continue
#             answer = _min_no_none(answer, min_coins_memoized(sub, coins) + 1)

#     return answer


def how_many_ways(target, coins):
    memo = defaultdict(lambda: 0)

    memo[0] = 1
    for i in range(1, target + 1):
        memo[i] = 0
        for coin in coins:
            sub = i - coin
            if sub < 0:
                continue
            memo[i] = memo[i] + memo[sub]

    return memo[target]


def all_coin_combs(target: int, coins: set[int]) -> dict[int, list[list[int]]]:
    def recurse(coins, target, current_combination, current_sum):
        if current_sum == target:
            result.append(list(current_combination))
            return
        if current_sum > target:
            return
        for coin in coins:
            current_combination.append(coin)
            recurse(coins, target, current_combination, current_sum + coin)
            current_combination.pop()

    result = []
    recurse(coins, target, [], 0)
    return {len(result): sorted(result, key=len)}


if __name__ == "__main__":
    target = 13
    s_coins = {1, 4, 5}

    print("~~ Coin Change Program ~~\n")
    print(f"Target Sum in Cents: {target}")
    print(f"Set of Coin values: {s_coins}")
    print()  # newline
    print(f"{min_num_of_coins(target, s_coins)=}")
    # print(f"{min_coins_memoized(target, s_coins)=}")
    print(f"{how_many_ways(target, s_coins)=}")
    print(f"{all_coin_combs(target, s_coins)=}")
    print("\nNext Steps, how to deduplicate unorder coin combo lists?")
    print(
        "[1,1,2], [1,2,1], and [2,1,1] are technically the same combo in different orders"
    )
