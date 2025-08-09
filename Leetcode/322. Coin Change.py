import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0

        if min(coins) > amount:
            return -1

        counts = [sys.maxsize] * (amount+1)
        counts[0] = 0
        for c in coins:
            if c <= amount:
                counts[c] = 1
                for i in range(c+1, amount+1):
                    if (counts[i - c] + counts[c]) < counts[i]:
                        counts[i] = counts[i - c] + counts[c]

        return counts[amount] if counts[amount] < sys.maxsize else -1

    def pickCoin(self, coins, idx, curr_amount, coin_count):
        # 종료 조건 확인
        if idx >= len(coins):  # 시작부터 목표 금액이 0인 경우
            return -1

        if curr_amount == 0:  # 목표 금액 맞출 시 코인 개수 반환
            return coin_count
        if curr_amount < 0: # 목표 금액 초과하면 -1
            return -1

        # 코인 선택
        pick = coins[idx]
        pick_curr = self.pickCoin(coins, idx, curr_amount - pick, coin_count + 1)
        pick_next = self.pickCoin(coins, idx + 1, curr_amount, coin_count)

        if pick_curr != -1 and pick_next != -1:
            return min(pick_curr, pick_next)
        else:
            if pick_curr != -1:
                return pick_curr
            else:
                return pick_next







print(Solution().coinChange([2], 1))
print(Solution().coinChange([3,7,405,436], 8839))
print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))