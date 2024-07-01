class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0

        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ")":
                if len(stack) == 0:
                    ans += 1
                else:
                    stack.pop()

        return ans + len(stack)

print(Solution().minAddToMakeValid(")))((("))