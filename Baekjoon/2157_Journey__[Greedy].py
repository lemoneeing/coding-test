import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().strip().split()) # 1 -> N, 'M 개 이하'의 도시만 방문, 총 K 개 항로
    path = [[] for _ in range(N+1)] # 방향 인접리스트
    for _ in range(K):
        a, b, c = map(int, input().strip().split())
        
        # 서 -> 동 이동은 거르기
        if a > b:
            continue

        if path[a]:
            path[a].append((b, c))
        else:
            path[a] = [(b, c)]
    
    dp = [[-1] * (N+1) for _ in range(M+1)] # dp[m][n]: m번 이동으로 n에 도달했을 때의 기내식 점수
    dp[1][1] = 0
    
    # m: 현재까지 방문한 도시의 수 (1개부터 M-1개까지 확인)
    for m in range(1, M):
        # i: 현재 있는 도시 번호
        for i in range(1, N + 1):
            # i번 도시에 m개 방문으로 도달한 적이 없다면 스킵
            if dp[m][i] == -1:
                continue
            
            # i번 도시에서 갈 수 있는 모든 항로 확인
            for nxt, score in path[i]:
                # i -> nxt 로 이동하면 총 m+1개의 도시를 방문하게 됨
                if dp[m+1][nxt] < dp[m][i] + score:
                    dp[m+1][nxt] = dp[m][i] + score
    
    ans = [dp[m][N] for m in range(1, M+1)]
    print(max(ans))

solve()