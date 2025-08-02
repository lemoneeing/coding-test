from typing import List

from selenium.webdriver.common.devtools.v118.page import CrossOriginIsolatedContextType


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        dist_r = homePos[0] - startPos[0]
        dist_c = homePos[1] - startPos[1]

        if dist_r < 0:
            totalRowCost = sum(rowCosts[startPos[0]+dist_r:startPos[0]])
        else:
            totalRowCost = sum(rowCosts[startPos[0]+1:startPos[0]+dist_r+1])

        if dist_c < 0:
            totalColCost = sum(colCosts[startPos[1]+dist_c:startPos[1]])
        else:
            totalColCost = sum(colCosts[startPos[1]+1:startPos[1]+dist_c+1])

        return totalRowCost + totalColCost


print(Solution().minCost([1,0], [2,3], [5,4,3], [8,2,6,7]))
print(Solution().minCost([0,0], [0,0], [5], [26]))
print(Solution().minCost([5,5], [5,2], [7,1,3,3,5,3,22,10,23], [5,5,6,2,0,16]))