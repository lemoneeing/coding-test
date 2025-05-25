from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans = []
        if x in nums:
            pivot = nums.index(x)

            for q in queries:
                if nums.count(x) < q:
                    ans.append(-1)
                    continue

                cnt = 0
                while pivot < len(nums) and cnt < q:
                    if nums[pivot] == x:
                        cnt += 1
                        pivot = nums[pivot+1:].index(x)

                ans.append(pivot)
        else:
            ans.append(-1)

        return ans

print(Solution().occurrencesOfElement([1,3,1,7],[1,3,2,4], 1))