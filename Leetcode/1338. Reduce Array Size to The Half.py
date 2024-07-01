from queue import PriorityQueue
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = []
        cal = {}
        for n in arr:
            if n in cal and cal[n]:
                continue

            cnt.append((arr.count(n), n))
            cal[n] = True

        cnt.sort(reverse=True)

        ans = []
        tLen = len(arr) // 2
        for curr in cnt:
            if len(arr) <= tLen:
                break

            while curr[1] in arr:
                arr.remove(curr[1])

            ans.append(curr[1])

        return len(ans)


print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(Solution().minSetSize([7,7,7,7,7,7]))
print(Solution().minSetSize([1000,1000,3,7]))
print(Solution().minSetSize([1,2,3,4,5,6,7,8,9,10]))