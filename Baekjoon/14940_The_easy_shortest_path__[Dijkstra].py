import sys
input = sys.stdin.readline

def solution():
    # 모든 정점에서 2 까지의 거리 계산(2는 단 하나)
    # = 2 에서 다른 모든 정점으로까지의 거리 계산 = 다익스트라
    # 모든 정점 사이의 거리가 1로 동일하므로 2를 중심으로 가장 가까운 곳부터 탐색해야 함. = BFS
    n, m = map(int, input().split())
    board = []
    dp = []
    visited = []
    start = None # 2의 위치
    for r in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        dp.append([-1 for _ in range(m)])
        visited.append([False for _ in range(m)])
        if 2 in row:
            start = (r, c := row.index(2))
            dp[r][c] = 0
            visited[r][c] = True

    dir_x = [-1, 0, 1, 0]
    dir_y = [0, 1, 0, -1]

    q = [start]
    while q:
        sx, sy = q.pop(0)
        for i in range(4):
            ex = sx + dir_x[i]
            ey = sy + dir_y[i]
            if 0 <= ex < n and 0 <= ey < m and not visited[ex][ey]:
                if board[ex][ey] == 0:
                    dp[ex][ey] = 0
                else:
                    if dp[ex][ey] == -1:
                        dp[ex][ey] = min(1000001, dp[sx][sy]+1)
                    q.append((ex, ey))

                visited[ex][ey] = True

    for r in range(n):
        for c in range(m):
            if dp[r][c] == -1 and board[r][c] == 0:
                sys.stdout.write(f"0 ")
            else:
                sys.stdout.write(f"{dp[r][c]} ")
        if r < n-1:
            sys.stdout.write(f"\n")

solution()