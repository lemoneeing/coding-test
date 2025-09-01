import sys

input = sys.stdin.readline

def solution():
    T, W, H = map(int, input().split())
    plums = [int(input()) for _ in range(T)]

    dp = [[0] * (W+1) for _ in range(T+1)]
    move = 0
    for t, p in enumerate(plums):
        t += 1

        for w in range(W+1):
            if w == 0:
                dp[t][w] = dp[t-1][w] + 1 if p == 1 else dp[t-1][w]
            else:
                if w % 2 == 0: # 나무 1
                    if p == 1: # 자두 겟
                        dp[t][w] = max(dp[t-1][w-1], dp[t-1][w]) + 1
                    else: # 자두 놓침
                        dp[t][w] = dp[t - 1][w]

                if w % 2 == 1: # 나무 2
                    if p == 1: # 자두 놓침
                        dp[t][w] = dp[t-1][w]
                    else: # 자두 겟
                        dp[t][w] = max(dp[t - 1][w - 1], dp[t - 1][w]) + 1

    sys.stdout.write(f"{max(dp[-1])}")

solution()
