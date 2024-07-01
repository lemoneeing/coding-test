from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]

        for i in range(len(pref)):
            if i == 0:
                continue

            arr.append(pref[i]^pref[i-1])

        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.findArray([5,2,0,3,1]))
