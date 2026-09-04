"""
Coin Change
--------------
You are given an integer array `coins` representing coins of different
denominations and an integer `amount` representing a total amount of
money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the
coins, return -1.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1

Example 2:
    Input: coins = [2], amount = 3
    Output: -1

Example 3:
    Input: coins = [1], amount = 0
    Output: 0

Constraints:
    1 <= len(coins) <= 12
    1 <= coins[i] <= 2^31 - 1
    0 <= amount <= 10^4
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
    return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    tests = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
    ]

    for coins, amount, expected in tests:
        result = coin_change(coins, amount)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: coin_change({coins}, {amount}) = {result} (expected {expected})")
