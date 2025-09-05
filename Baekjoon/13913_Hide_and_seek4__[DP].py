import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    # N 보다 작은 수로 갈 때에는 1칸씩 이동하는 방법 뿐
    if N >= K:
        sys.stdout.write(f"{N - K}\n")

        if N == K:
            sys.stdout.write(f"{N} {K}")
        else:
            for i in range(N, K-1, -1):
                sys.stdout.write(f"{i} ")
        return

    if abs(K-N) == 1:
        sys.stdout.write(f"1\n")
        sys.stdout.write(f"{N} {K}")

    else:
        dp = [sys.maxsize] * ((K - 1) * 2)
        dp[N] = 0
        if N > 0:
            dp[N-1] = dp[N+1] = 1
            dp[:N-1] = [i for i in range(N, 1, -1)]
        else:
            dp[N + 1] = 1
        path = [-1] * ((K - 1) * 2)
        path[:N] = [j for j in range(1, N+1)]
        path[N+1] = N
        for i in range(N+2, (K - 1) * 2):
            if i % 2 == 0:
                tmp_no = [i-1, i+1, i//2]
                tmp_dp = [dp[i-1], dp[i+1], dp[i // 2]]
                min_v = min(tmp_dp)
                dp[i] = min_v + 1
                path[i] = tmp_no[tmp_dp.index(min_v)]
            else:
                dp[i] = min(dp[i - 1]+1, dp[(i+1) // 2] + 2)
                tmp_no = [i-1, (i+1)//2]
                tmp_dp = [dp[i - 1]+1, dp[(i+1) // 2] + 2]
                min_v = min(tmp_dp)
                dp[i] = min_v
                path[i] = tmp_no[tmp_dp.index(min_v)]

        sys.stdout.write(f"{dp[K]}\n")
        ans = [K]
        j = K
        while j != -1:
            ans.append(path[j])
            j = path[j]
        sys.stdout.write(f"{' '.join(map(str, reversed(ans[:-1])))}")

solution()
