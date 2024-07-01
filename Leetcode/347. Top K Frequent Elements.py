from typing import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # frq = {}
        # for n in nums:
        #     cnt = nums.count(n)
        #     if cnt in frq:
        #         if not n in frq[cnt]:
        #             frq[cnt].append(n)
        #     else:
        #         frq[cnt]= [n]
        #
        # tmp = sorted(list(frq.keys()), reverse=True)
        #
        # answer = [set(frq[k]) for k in tmp[:2]]

        return [k for k, v in collections.Counter(nums).most_common(k)]

if __name__ == "__main__":
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
