import sys

def solution():
    dp = [1] * 10001 # 1로만 이루어진 경우의 수 = 1
    for i in range(2, 10001):
        dp[i] += dp[i - 2]
        
    for i in range(3, 10001):
        dp[i] += dp[i - 3]
        
    # # dp[n] = 1(1로만 이루어진 경우의 수) + dp[n-2](현재 수보다 2만큼 작은 수의 경우의 수) + dp[n-3](현재 수보다 3만큼 작은 수의 경우의 수)
    # dp[1] = 1   # 1
    # dp[2] = 2   # 1+1   / 2
    # dp[3] = 3   # 1+1+1 / 2+1 / 3
    # for i in range(4, 10001):
    #     dp[i] = dp[i] + dp[i-2] + dp[i-3]
        
    tc = int(sys.stdin.readline())
    for _ in range(tc):
        goal = int(sys.stdin.readline())
        sys.stdout.write(f"{dp[goal]}\n")
        
solution()