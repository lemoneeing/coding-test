import sys

input = sys.stdin.readline


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        hint_a = 0
        hint_b = 0

        # secret 과 guess 를 한 번씩 순회하여 각 구성 숫자의 인덱스를 기록
        secret_stat = {}
        for i, s in enumerate(secret):
            s_stat = secret_stat.get(int(s), [])
            s_stat.append(i)
            secret_stat[int(s)] = s_stat

        guess_stat = {}
        for j, g in enumerate(guess):
            g_stat = guess_stat.get(int(g), [])
            g_stat.append(j)
            guess_stat[int(g)] = g_stat

        for n, pos_in_s in secret_stat.items():
            pos_in_g = guess_stat.get(n, [])
            if pos_in_g:
                if pos_in_g == pos_in_s: # 모든 n 의 위치가 다 일치 => bulls
                    hint_a += len(pos_in_s)
                else:
                    bulls_cnt = len(set(pos_in_s).intersection(pos_in_g))
                    if bulls_cnt: # 일부 n 의 위치만 일치 => 일치하는 수만큼 bulls
                        hint_a += bulls_cnt

                    if len(pos_in_s) - bulls_cnt > 0 and len(pos_in_g) - bulls_cnt > 0:
                            hint_b += min(len(pos_in_g)-bulls_cnt, len(pos_in_s)-bulls_cnt)

        return f"{hint_a}A{hint_b}B"


print(Solution().getHint("1807", "7810"))
print(Solution().getHint("1123", "0111"))
print(Solution().getHint("11", "10"))
