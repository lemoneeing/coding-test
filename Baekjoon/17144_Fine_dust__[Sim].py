import sys
input = sys.stdin.readline


def solution():
    R, C, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]
    dust = [(r, c) for r in range(R) for c in range(C) if grid[r][c] > 0]
    purifier = [r for r in range(R) if grid[r][0] == -1]

    # 미세먼지 확산
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for t in range(T):
        diffusion = [[[0, 0, 0, 0, 0] for _ in range(C)] for __ in range(R)]
        for dstr, dstc in dust:
            dff = grid[dstr][dstc] // 5     # 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
            diffusion[dstr][dstc][0] = dff
            dff_cnt = 0
            for i, (dr, dc) in enumerate(dir):
                mr = dstr + dr
                mc = dstc + dc

                # 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
                if 0 <= mr < R and 0 <= mc < C and grid[mr][mc] >= 0:
                    dff_cnt += 1  # 확산할 방향 수
                    diffusion[dstr][dstc][i+1] = 1
                    if (mr, mc) not in dust:
                        dust.append((mr, mc))  # 먼지가 없던 곳에 먼지 확산 시 dust 에 추가
            # (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.
            grid[dstr][dstc] -= (dff * dff_cnt)

        # (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
        for r, arr in enumerate(diffusion):
            for c, info in enumerate(arr):
                if info[0] > 0:
                    for i, is_diffused in enumerate(info[1:]):
                        if is_diffused:
                            rr = r + dir[i][0]
                            cc = c + dir[i][1]
                            grid[rr][cc] += info[0]
        pass


        ############ 위쪽 공기청정기의 바람은 반시계방향으로 순환하고,
        # 공기청정기 윗 영역 아래 방향
        for r in range(purifier[0]-1, 0, -1):
            grid[r][0] = grid[r-1][0]

        # 공기청정기 윗 영역 왼방향
        left_start = grid[0][0]
        grid[0][:-1] = grid[0][1:]
        grid[1][0] = left_start

        # 공기청정기 윗 영역 위 방향
        up_end = grid[0][-1]
        for r in range(purifier[0]):
            grid[r][-1] = grid[r+1][-1]
        grid[0][-2] = up_end

        # 공기청정기 윗 영역 오른쪽 방향
        right_end = grid[purifier[0]][-1]
        grid[purifier[0]][2:] = grid[purifier[0]][1:-1]
        grid[purifier[0]][1] = 0
        grid[purifier[0]-1][-1] = right_end


        ############ 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
        # 공기청정기 아래 영역 위 방향
        for r in range(R-1, purifier[1]+1, -1):
            grid[r-1][0] = grid[r][0]

        #공기청정기 아래 영역 왼방향
        left_end = grid[-1][0]
        grid[-1][:-1] = grid[-1][1:]
        grid[-2][0] = left_end

        # 공기청정기 아래 영역 아래 방향
        for r in range(R-1, purifier[1]+1, -1):
            grid[r][-1] = grid[r-1][-1]

        # 공기청정기 아래 영역 오른쪽 방향
        grid[purifier[1]+1][-1] = grid[purifier[1]][-1]
        grid[purifier[1]][2:] = grid[purifier[1]][1:-1]
        grid[purifier[1]][1] = 0

    ans = 0
    for last_r in grid:
        ans += sum(last_r)

    sys.stdout.write(f"{ans}")

solution()
