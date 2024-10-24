import sys

def solution():
    R, C = map(int, sys.stdin.readline().strip().split())
    treasure_map = []
    land_cnt = 0
    for _ in range(R):
        treasure_map.append(list(sys.stdin.readline().strip()))
        land_cnt += treasure_map[-1].count('L')

    if land_cnt == R * C:
        sys.stdout.write(f"{R+C-2}")
        return

    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)
    path_weight = [[0]*C for _ in range(R)]
    v = [[False]*C for _ in range(R)]
    tmp_mx = 0
    q = []
    for r in range(R):
        for c in range(C):
            if treasure_map[r][c] == 'W':
                continue

            q.append((r, c))
            v[r][c] = True
            while q:
                curr_pos = q.pop(0)
                for d in range(4):
                    nr = curr_pos[0] + dr[d]
                    nc = curr_pos[1] + dc[d]

                    if nr >= 0 and nr < R and nc >= 0 and nc < C:
                        if treasure_map[nr][nc] == 'L' and not v[nr][nc]:
                            path_weight[nr][nc] = path_weight[curr_pos[0]][curr_pos[1]] + 1
                            v[nr][nc] = True
                            q.append((nr, nc))
                            if tmp_mx < path_weight[nr][nc]:
                                tmp_mx = path_weight[nr][nc]

            path_weight = [[0] * C for _ in range(R)]
            v = [[False]*C for _ in range(R)]

    sys.stdout.write(f"{tmp_mx}")
solution()