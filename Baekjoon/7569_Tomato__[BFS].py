import sys
from collections import deque
input = sys.stdin.readline

def solution():
    M, N, H = map(int, input().split())
    floors = []
    reds = deque()
    red_cnt = 0
    empty_cnt = 0
    for h in range(H):
        box = []
        for r in range(N):
            row = list(map(int, input().split()))
            box.append(row)
            for c, tom in enumerate(row):
                if tom == 1:
                    reds.append((h, r, c, 0))
                    red_cnt += 1
                elif tom == -1:
                    empty_cnt += 1
        floors.append(box)

    dir = [(0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
    while reds:
        h, n, m, day = reds.popleft()
        for z, x, y in dir:
            if 0 <= h+z < H and 0<= n+x < N and 0 <= m+y < M and floors[h+z][n+x][m+y] == 0:
                floors[h+z][n+x][m+y] = 1
                red_cnt += 1
                reds.append((h+z, n+x, m+y, day+1))

    if red_cnt == H * M * N - empty_cnt:
        sys.stdout.write(f"{day}")
    else:
        sys.stdout.write("-1")

solution()
