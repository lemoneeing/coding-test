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

    # 두 지점 사이의 차가 1이면 단순 출력으로 해결
    if abs(K-N) == 1:
        sys.stdout.write(f"1\n")
        sys.stdout.write(f"{N} {K}")

    else:
        # dp배열 초기화: dp배열 = N 에서 각 지점까지 최소 이동 횟수
        dp = [sys.maxsize] * ((K - 1) * 2)
        dp[N] = 0
        if N > 0:
            dp[:N] = [i for i in range(N, 0, -1)] # N -> 0 까지는 N(이동횟수 0)에서 1칸씩 이동(이동횟수 1씩 증가)
        dp[N + 1] = 1 # N 바로 다음 칸. 1칸 이동으로 도착하는 것이 최소 이동 횟수이므로 초기화

        # 경로 추적. path[x] = (x지점에 최소 이동 횟수로 도달하기 위한 이전 지점)
        path = [-1] * ((K - 1) * 2)
        path[:N] = [j for j in range(1, N+1)]
        path[N+1] = N

        for i in range(N+2, (K - 1) * 2):
            # 탐색 위치가 짝수일 때 이전 경로가 될 수 있는 위치: 바로 앞(홀), 뒤(홀), 1/2(홀,짝) 위치 -> 이 중에서 최소 횟수 탐색
            if i % 2 == 0:
                tmp_no = [i-1, i//2]
                tmp_dp = [dp[i-1], dp[i // 2]]
                min_v = min(tmp_dp)
                dp[i] = min_v + 1
                path[i] = tmp_no[tmp_dp.index(min_v)]
            # 탐색 위치가 홀수일 때 이전 경로가 될 수 있는 위치: 바로 앞(짝), 뒤(짝) -> 뒤(짝)의 이동횟수 = '뒤' 위치의 절반인 위치의 이동횟수 + 2
            else:
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
