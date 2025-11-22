import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    grid = []
    cheese_cnt = 0
    for _ in range(N):
        line = list(map(int, input().split()))
        cheese_cnt += line.count(1)
        grid.append(line)

    ans = 0
    while True:
        # 모눈종이를 빈 공간 위주로 탐색. 마주친 치즈 면에는 마주친 횟수만큼 갱신
        visited = [[0]*M for _ in range(N)]
        q = [(0, 0)]
        q_size = 1
        visited[0][0] = 1
        while q:
            for _ in range(q_size):
                r, c = q.pop(0)
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < M:
                        if not visited[nr][nc] and grid[nr][nc] == 0:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                        elif grid[nr][nc] == 1:
                            visited[nr][nc] += 1
        
        # visited 가 2 이상인 칸을 빈 공간(0) 으로 갱신
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1 and visited[r][c] >= 2:
                    grid[r][c] = 0
                    cheese_cnt -= 1
        ans += 1

        if cheese_cnt == 0:
            break

    print(ans)
    
solution()
