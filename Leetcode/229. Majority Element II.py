from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        size = len(nums)
        criteria = size//3

        cnt_arr = {}
        for n in nums:
            cnt = cnt_arr.get(n, 0) + 1
            cnt_arr.update({n:cnt})

        ans = [n for n, c in cnt_arr.items() if c > criteria]

        return ans

print(Solution().majorityElement())
