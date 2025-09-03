import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    # N 보다 작은 수로 갈 때에는 1칸씩 이동하는 방법 뿐
    if N > K:
        sys.stdout.write(f"{N-K}")
        for i in range(N, K-1, -1):
            sys.stdout.write(f"{i} ")
        return

    dp = [sys.maxsize] * (K * 2 + 1)
    dp[N] = 0
    dp[N-1] = dp[N+1] = 1
    dp[:N-1] = [i for i in range(N, 1, -1)]
    path = [-1] * (K * 2)
    path[N+1] = N
    for i in range(N+2, 2*K):
        if i % 2 == 0:
            dp[i] = min(dp[i-1], dp[i+1], dp[i // 2]) + 1
        else:
            dp[i] = min(dp[i - 1]+1, dp[(i+1) // 2] + 2)

        # dp[i - 1] = min(dp[i-1], dp[i - 2] + 1, dp[i] + 1)

    sys.stdout.write(f"{dp[K]}")

solution()
