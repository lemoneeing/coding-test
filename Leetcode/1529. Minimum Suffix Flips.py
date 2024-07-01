class Solution:
    def minFlips(self, target: str) -> int:

        flip = 0
        ans = 0

        for s in target:
            n = int(s)
            if n ^ flip: # flip 발생 -> ans 1 추가
                ans += 1
                flip ^= 1 # flip 이 0부터 시작하므로 (?)