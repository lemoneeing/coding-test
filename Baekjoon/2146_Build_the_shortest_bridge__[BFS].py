import sys
import copy

def solution():
    N = int(sys.stdin.readline())
    wm = []
    for _ in range(N):
        wm.append(list(map(int, sys.stdin.readline().split())))

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
                c_r, c_c = q.pop(0) # 현재 위치
                for x, y in zip(dx, dy):
                    nx_r = c_r+y
                    nx_c = c_c+x
                    # 범위 내 존재 + 바다가 아닌 곳 = 현재 위치와 이어진 섬
                    if 0 <= nx_r < N and 0 <= nx_c < N and not visited[nx_r][nx_c] and wm[nx_r][nx_c] != 0:
                        wm[nx_r][nx_c] = isl_id
                        q.append((nx_r, nx_c)) # 다음 탐색 위치 = 0 보다 큰 값의 좌표
                        visited[nx_r][nx_c] = True

            isl_id -= 1

    # 가장 짧은 다리 찾기 (bfs)
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
            # 최초: 현재 거리(dist) 내에서 탐색 가능한 위치(1)만 저장 -> 탐색 도중: 현재 거리 내에서  탐색 가능한 위치 + 다음 거리(dist+1) 내에서 탐색 가능한 위치
            while q:
                limit = len(q) # 현재 거리(dist) 내에서 탐색 가능한 위치들만 선별히기 위한 장치
                dist += 1

                # 현재 거리 내에서 탐색 가능한 위치만 pop되므로 이 loop을 탈출하면 q에 남게 되는 위치는 다음 거리 내에서 탐색 가능한 위치만 남게 됨.
                for i in range(limit):
                    cr, cc = q.pop(0)
                    for dc, dr in zip(dx, dy):
                        nr = cr + dr
                        nc = cc + dc

                        # 범위 내 존재 + 출발 섬과 같지 않은 위치
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and wm[nr][nc] != wm[r][c]:
                            if wm[nr][nc] < 0: # 각 섬의 id 는 음수 값
                                arrival = True
                                break # 가장 빠르게 찾아낸 다른 섬이므로 더 이상 탐색 필요 없음.
                            q.append((nr, nc))
                            visited[nr][nc] = True

                    if arrival: # loop 를 한 번 더 탈출하기 위해
                        shortest_dist = min(shortest_dist, dist)
                        break

    sys.stdout.write(f"{shortest_dist}")

solution()