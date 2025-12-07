import sys
from copy import deepcopy

input = sys.stdin.readline

observ_dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 감시 방향: 상 우 하 좌
cctv_dirs = [
    [[0], [1], [2], [3]],  # 1번 CCTV 감시 방향 목록
    [(0, 2), (1, 3)],  # 2번 CCTV
    [(0, 1), (1, 2), (2, 3), (3, 0)],  # 3번 CCTV
    [(0, 1, 3), (1, 2, 0), (2, 3, 1), (3, 0, 2)],  # 4번 CCTV
    [(0, 1, 2, 3)]  # 5번 CCTV
]
min_blind_spots = 65
def count_blind_spot(office):
    blind_spot = 0
    for row in office:
        blind_spot += row.count(0)

    return blind_spot


def check_observe_spot(cctv_r, cctv_c, dir_types, office):
    obsv_space = 0

    for dir_idx in dir_types:
        n_r = cctv_r + observ_dirs[dir_idx][0]
        n_c = cctv_c + observ_dirs[dir_idx][1]

        while 0 <= n_r < len(office) and 0 <= n_c < len(office[0]):
            if office[n_r][n_c] == 6:
                break
            elif office[n_r][n_c] == 0: # 완전히 빈 칸일 때에만 카운팅
                office[n_r][n_c] = '#'
                obsv_space += 1

            n_r += observ_dirs[dir_idx][0]
            n_c += observ_dirs[dir_idx][1]

    return obsv_space


def rotate_cctv(cctvs, depth, office):
    global min_blind_spots

    if depth == len(cctvs):
        min_blind_spots = min(count_blind_spot(office), min_blind_spots)
        return

    cctv_r, cctv_c = cctvs[depth]
    cctv_type = office[cctv_r][cctv_c]
    for dir_types in cctv_dirs[cctv_type - 1]:
        office_map = deepcopy(office)
        check_observe_spot(cctv_r, cctv_c, dir_types, office_map)

        rotate_cctv(cctvs, depth + 1, office_map)



def solution():
    global min_blind_spots

    N, M = list(map(int, input().split()))
    office = []
    cctv_pos = []
    for r in range(N):
        ofc_row = list(map(int, input().split()))
        for c, v in enumerate(ofc_row):
            if 0 < v < 6:
                cctv_pos.append([r, c])
        office.append(ofc_row)

    min_blind_spots = N * M

    # 백트래킹
    rotate_cctv(cctv_pos, 0, office)

    print(min_blind_spots)

solution()
