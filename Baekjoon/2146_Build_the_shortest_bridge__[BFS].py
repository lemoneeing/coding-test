import sys
import copy

def solution():
    N = int(sys.stdin.readline())
    wm = []
    # visited = []
    for _ in range(N):
        wm.append(list(map(int, sys.stdin.readline().split())))
        # visited.append([False for __ in range(N)])

    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)

    # 각 섬별로 그룹핑(bfs)
    isl_id = -1
    visited = [[False]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if wm[r][c] <= 0:
                continue

            # 탐색 출발점 초기화
            q = [(r, c)]
            visited[r][c] = True
            wm[r][c] = isl_id
            while q:
                c_r, c_c = q.pop(0)
                for x, y in zip(dx, dy):
                    nx_r = c_r+y
                    nx_c = c_c+x
                    if 0 <= nx_r < N and 0 <= nx_c < N and not visited[nx_r][nx_c] and wm[nx_r][nx_c] != 0:
                        wm[nx_r][nx_c] = isl_id
                        q.append((nx_r, nx_c)) # q 에는 0 보다 큰 타일의 좌표만 저장됨.
                        visited[nx_r][nx_c] = True

            isl_id -= 1

    # 가장 짧은 다리 찾기 (bfs)
    shortest_br = sys.maxsize
    shortest_dist = sys.maxsize
    for r in range(N):
        for c in range(N):
            if wm[r][c] == 0:
                continue

            q = [(r, c)]
            visited = [[False]*N for _ in range(N)]
            visited[r][c] = True
            dist = -1
            arrival = False
            while q:
                limit = len(q)
                dist += 1
                for i in range(limit):
                    cr, cc = q.pop(0)
                    for dc, dr in zip(dx, dy):
                        nr = cr + dr
                        nc = cc + dc

                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and wm[nr][nc] != wm[r][c]:
                            if wm[nr][nc] < 0:
                                arrival = True
                                break
                            q.append((nr, nc))
                            visited[nr][nc] = True

                    if arrival:
                        shortest_dist = min(shortest_dist, dist)
                        break


    sys.stdout.write(f"{shortest_dist}")
    pass

solution()