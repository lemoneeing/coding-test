class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_cnt = {}
        for tt in t:
            cnt = t_cnt.get(tt, 0)
            t_cnt.update({tt: cnt+1})

        if len(s) == len(t) == 1:
            if s == t:
                return s
            else:
                return ""

        # ans = ""
        # for i in range(0, len(s)-len(t)+1):
        #     for j in range(i+len(t), len(s)+1):
        #         find = True
        #         subs = s[i:j] if j < len(s) else s[i:]
        #         for ch, cnt in t_cnt.items():
        #             if subs.count(ch) < cnt:
        #                 find = False
        #                 break
        #         if find and (not ans or len(ans) > j-i):
        #             ans = subs

        i = 0
        j = i + len(t)
        ans = ""
        while i < j <= len(s):
            find = True
            subs = s[i:j] if j < len(s) else s[i:]
            for tt, cnt in t_cnt.items():
                if subs.count(tt) < cnt:
                    j += 1
                    find = False
                    break

            if find:
                if not ans or len(ans) > j - i:
                    ans = subs
            else:
                i += 1
                if j > len(s):
                    j = i + len(t)
                    break

        return ans

print(Solution().minWindow("ADOBECODEBANC", "ABC"))
# print(Solution().minWindow("A", "B"))
print(Solution().minWindow("A", "A"))
# print(Solution().minWindow("A", "AA"))
print(Solution().minWindow("AB", "B"))
print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
# print(Solution().minWindow("babb", "baba"))
