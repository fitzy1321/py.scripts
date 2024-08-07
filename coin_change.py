#!/usr/bin/env python3

from functools import lru_cache
from collections import defaultdict


def _min_no_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


def min_coins(target, coins):
    if not hasattr(min_coins, "memo"):
        min_coins.memo = {}

    try:
        return min_coins.memo[target]
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
            answer = _min_no_none(answer, min_coins(sub, coins) + 1)  # type: ignore

    min_coins.memo[target] = answer
    return answer


@lru_cache
def min_coins_memoized(target: int, coins: frozenset[int]):
    if target == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            sub = target - coin
            if sub < 0:
                continue
            answer = _min_no_none(answer, min_coins_memoized(sub, coins) + 1)

    return answer


def how_many_possibilities(target: int, coins: set[int]) -> int:
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


def _dedup_combos(combo_list: list[list[int]]) -> list[list[int]]:
    sameses: dict[tuple[int, frozenset[int]], list[int]] = {}
    for coins in combo_list:
        key = (len(coins), frozenset(coins))
        sameses[key] = coins
    return list(sameses.values())


def deduplicated_combos(target: int, coins: set[int]) -> dict[int, list[list[int]]]:
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
    final = _dedup_combos(result)
    return {len(final): final}


if __name__ == "__main__":
    target = 13
    s_coins = {1, 4, 5}

    print("~~ Coin Change Program ~~\n")
    print(f"Target Sum in Cents: {target}")
    print(f"Set of Coin values: {s_coins}")
    print()  # newline
    print(f"{min_coins(target, s_coins)=}")
    print(f"{min_coins_memoized(target, frozenset(s_coins))=}")
    print(f"{how_many_possibilities(target, s_coins)=}")
    print(f"{deduplicated_combos(target, s_coins)=}")
