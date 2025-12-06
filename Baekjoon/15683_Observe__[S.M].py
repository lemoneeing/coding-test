import sys
input = sys.stdin.readline

observ_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 감시 방향: 상 우 하 좌
cctv_dirs = [
    [1],        # 1번 CCTV
    [1, 3],     # 2번 CCTV
    [0, 1],     # 3번 CCTV
    [0, 1, 3],  # 4번 CCTV
    [0, 1, 2]   # 5번 CCTV
]

r_rot_dirs_idx = [1, 2, 3, 0]
l_rot_dirs_idx = [3, 0, 2, 2]

def solution():
    N, M = list(map(int, input().split()))
    office = []
    for _ in range(N):
        office.append(list(map(int, input().split())))

    blind_spot = N * M

    for r in range(N):
        for c in range(M):
            if office[r][c] != 0 and office[r][c] != 6:
                cctv = office[r][c] - 1
                obs_idx = cctv_dirs[cctv]

                for






solution()
