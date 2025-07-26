from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        ans = []
        for idx in range(10, len(s), 1):
            ten_subs = s[idx-10:idx]

            if ten_subs not in ans:
                if ten_subs in s[idx-10+1:]:
                    ans.append(ten_subs)

        return ans

print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA"))
