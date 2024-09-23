import sys
from collections import Counter
def solution():
    N, K = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    dp = [0 for _ in range(N)]

    for e in range(N, 1, -1):
        if Counter(arr[:e]).most_common(n=1)[0][-1] <= K:
            dp[0] = len(arr[:e])
            break

    for i in range(N, e, -1):
        most = Counter(arr[e:i]).most_common(n=1)
        if most[0][-1] <= K:
            if Counter(arr[i-1:(i-1)+dp[i-1]]).most_common(n=1)[0][-1] <= K:
                dp[i] = max(dp[i-1]+1, len(arr[i:i+e]))
            else:
                dp[i] = len(arr[i:i+e])
        else:
            dp[i] = dp[i-1] - 1

    sys.stdout.write(f"{max(dp)}")

solution()