import sys

input = sys.stdin.readline


def solution():
    N, L, R = map(int, input().split())
    n_map = []
    visited = [False] * (N * N)

    for i in range(N):
        n_map.append(list(map(int, input().strip().split())))


    # BFS 로 연합 짓기
    def bfs(r, c): # 시작점 r, c 에 대해 모든 연합 국가 찾기
        nonlocal N, L, R, n_map

        q = [(r, c)]
        union = [(r, c)]
        population = n_map[r][c]

        d_r = [-1, 0, 1, 0]
        d_c = [0, 1, 0, -1]

        while q:
            curr_r, curr_c = q.pop(0)

            for i in range(4):
                next_r = curr_r + d_r[i]
                next_c = curr_c + d_c[i]
                next_idx = (next_r * N) + next_c

                if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N:
                    continue

                if not visited[next_idx] and L <= abs(n_map[curr_r][curr_c] - n_map[next_r][next_c]) <= R:
                    union.append((next_r, next_c))
                    q.append((next_r, next_c))
                    population += n_map[next_r][next_c]
                    visited[next_idx] = True

        if len(union) <= 1:
            return 0

        for row, col in union:
            n_map[row][col] = population // len(union) # 연합한 국가들에 대해서만 인구 이동

        return 1


    ans = 0
    while True:
        movement = False
        for i in range(N):
            for j in range(N):
                if not visited[i * N + j]:
                    visited[i * N + j] = True
                    movement = True if bfs(i, j) > 0 else movement

        if movement:
            ans += 1
            visited = [False] * (N * N)
        else:
            break

    print(ans)

solution()