#!/usr/bin/env python3

from functools import lru_cache
from collections import defaultdict
from timeit import timeit
from typing import AbstractSet

import cProfile
import pstats


def _min_no_none(a, b):
    a_is_none = a is None
    b_is_none = b is None
    if a_is_none and b_is_none:
        raise ValueError("At least one value is needed")
    if a_is_none:
        return b
    if b_is_none:
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


def how_many_possibilities(target: int, coins: AbstractSet[int]) -> int:
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
    for combo in combo_list:
        key = (len(combo), frozenset(combo))
        sameses[key] = combo
    return list(sameses.values())


def _dedup_combos_v2(combo_list: list[list[int]]) -> list[list[int]]:
    sameses: dict[tuple[int, frozenset[int]], list[int]] = {}
    for combo in combo_list:
        key = (len(combo), frozenset(combo))
        # this is _technically_ faster, but only by miliseconds, so may not be worth it ...
        if key in sameses:
            continue
        sameses[key] = combo
    return list(sameses.values())


@lru_cache
def full_list_possibilities(target: int, coins: frozenset[int]) -> list[list[int]]:
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
    return result


def normalized_possibilities(
    target: int,
    coins: frozenset[int],
) -> dict[int, list[list[int]]]:
    # TODO: I should throw this function into a flame graph
    result = full_list_possibilities(target, coins)
    final = _dedup_combos_v2(result)
    return {len(final): sorted(final, key=len)}


if __name__ == "__main__":
    target = 55
    coin_set = frozenset([1, 5, 10, 25, 50])

    print("~~ Coin Change Program ~~\n")
    print(f"Target Sum in Cents: {target}")
    print(f"Set of Coin values: {coin_set}")
    print()  # newline
    with cProfile.Profile() as profile:
        print(f"{min_coins(target, coin_set)=}")
        print(f"{min_coins_memoized(target, coin_set)=}")
        print(f"{how_many_possibilities(target, coin_set)=}")
        print(f"{normalized_possibilities(target, coin_set)=}")

        combos = full_list_possibilities(target, coin_set)
        print("Attempts to optimize the deduplication function: smaller is better")
        print(f"{timeit(lambda: _dedup_combos(combos), number=5)=}")
        print(f"{timeit(lambda: _dedup_combos_v2(combos), number=5)=}")

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats()
    results.dump_stats("build/coin_change_perf.prof")
    # in shell:
    # # pip install -U tuna
    # tuna build/coin_change_perf.prof
