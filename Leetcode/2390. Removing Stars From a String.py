class Solution:
    def removeStars(self, s: str) -> str:

        ans = ''

        for c in s:
            if c != '*':
                ans += c
            else:
                ans = ans[:-1]
        return ans

if __name__ == "__main__":
    print(Solution().removeStars("erase*****"))