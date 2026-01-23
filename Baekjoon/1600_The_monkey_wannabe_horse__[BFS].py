from collections import deque

HORSE_MOVING = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

def move_like_horse(dir_idx, px, py, grid):
    "말처럼 움직이기, 장애물은 점프 가능"

    rows = len(grid)
    cols = len(grid[0])

    dx, dy = HORSE_MOVING[dir_idx]

    nx, ny = px, py
    
    ox = 0
    for nx in range(dx):
        while nx < rows and grid[nx][ny] == 1:
            ox +=1
        
        if nx >= rows:
            return px, py

    for oy in range(dy):
        ny += oy

        while ny < cols and grid[nx][ny] == 1:
            ny += 1

        if ny >= cols:
            return px, py

    return nx, ny
    

def solve():
    K = int(input())
    W, H = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(int, input().split())))

    moving = [[[-1] * W for _ in range(H)] for __ in range(K+1)]
    q = deque([(0, 0, 0)])
    moving[0][0][0] = 0
    while q:
        cr, cc, jumps = q.popleft()

        if cr == H-1 and cc == W-1:
            print(moving[jumps][cr][cc])
            return
        
        curr_dist = moving[jumps][cr][cc]

        # 원숭이 이동
        for mr, mc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = cr + mr
            nc = cc + mc

            if 0 <= nr < H and 0<= nc < W and grid[nr][nc] == 0 and moving[jumps][nr][nc] == -1:
                moving[jumps][nr][nc] = curr_dist + 1
                q.append((nr, nc, jumps))
        
        # 말 이동
        if jumps < K:
            jumps += 1
            for hr, hc in HORSE_MOVING:
                nr = cr + hr
                nc = cc + hc

                if 0 <= nr < H and 0<= nc < W and grid[nr][nc] == 0 and moving[jumps][nr][nc] == -1:
                    moving[jumps][nr][nc] = curr_dist + 1
                    q.append((nr, nc, jumps))

    print(-1)

solve()