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

rot_dirs_idx = [1, 2, 3, 0]
# l_rot_dirs_idx = [3, 0, 2, 2]

def rotate_cctv(cctv_r, cctv_c, board):
    
    obs_space = 0
    cctv_type = board[cctv_r][cctv_c]

    for curr_dir_type in cctv_dirs[cctv_type-1]:
        next_dir_type = curr_dir_type % 4 + 1
        obs_r, obs_c = observ_dirs[next_dir_type] 
        
        board[cctv_r + obs_r][cctv_c+obs_c] = '#' 
        obs_space += 1

    return obs_space


def solution():
    N, M = list(map(int, input().split()))
    office = []
    cctv_pos = []
    for r in range(N):
        ofc_row = list(map(int, input().split()))
        for c, v in enumerate(ofc_row):
            if 0 < v < 6:
                cctv_pos.append((r, c))
        office.append(ofc_row)

    blind_spot = N * M

    # 백트래킹
    for cctv in cctv_pos:
        for i in range(4):
            blind_spot -= rotate_cctv(cctv[0], cctv[1], office)
    






solution()
