import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    mems = list(map(int, sys.stdin.readline().split()))
    costs = list(map(int, sys.stdin.readline().split()))

    # 예시)
    # 5 60
    # 30 10 20 35 40
    # 3 0 3 5 1

    # 비활성화 시나리오
    # mems[0][4] = app0 ~ 4 를 비활성화 했을 때 확보할 수 있는 여유 공간
    # mems[
    #    0          1             2               3 4
    # 0 [0]  min(+[1], '')  min(+[2], '')        6 6 4

    dp = [sys.maxsize] * N
    dp[0] =
    for i in range(N):

        dp[i] = min(dp[i-1] + costs[i], dp[i-1])

