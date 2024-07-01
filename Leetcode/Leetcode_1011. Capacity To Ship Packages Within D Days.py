from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
        # Output: 15
        # Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
        # 1st day: 1, 2, 3, 4, 5
        # 2nd day: 6, 7
        # 3rd day: 8
        # 4th day: 9
        # 5th day: 10

        # 짐 수량 // 운반기간 == 하루 최소 운반 짐 수량
