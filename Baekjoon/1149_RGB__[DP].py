import sys
def solution():
    N = int(sys.stdin.readline())
    h = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[0, 0, 0] for _ in range(N)]
    dp[0][0] = h[0][0]
    dp[0][1] = h[0][1]
    dp[0][2] = h[0][2]

    for i in range(1, N):
        for j in range(3):
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + h[i][j]

    return min(dp[N-1])

print(solution())