from functools import cache
from collections import defaultdict


def min_no_none(a: int | None, b: int | None):
    if a is None:
        return b
    if b is None:
        return a
    return int(min(a, b))


def min_coins(max_x: int, coins: set[int]):
    answer = 0
    if max_x == 0:
        return answer
    else:
        for coin in coins:
            sub = max_x - coin
            if sub < 0:
                continue
            answer = min_no_none(answer, min_coins(sub, coins) + 1)

    return answer


@cache
def min_coins_memoized(max_x: int, coins: set[int]):
    answer = 0
    if max_x == 0:
        return answer
    else:
        for coin in coins:
            sub = max_x - coin
            if sub < 0:
                continue
            answer = min_no_none(answer, min_coins_memoized(sub, coins) + 1)

    return answer


def how_many_ways(m, coins):
    memo = defaultdict(lambda: 0)

    memo[0] = 1
    for i in range(1, m + 1):
        memo[i] = 0
        for coin in coins:
            sub = i - coin
            if sub < 0:
                continue
            memo[i] = memo[i] + memo[sub]

    return memo[m]


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
    return {len(result): result}


print(all_coin_combs(4, {1, 2, 5}))
print("Next Steps, how to deduplicate unorder coin combo lists?")
print(
    "[1,1,2], [1,2,1], and [2,1,1] are technically the same combo in different orders"
)
