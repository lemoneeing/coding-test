import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())

    city = []
    houses = [] # 각 집의 좌표 저장. 인덱스 = 각 집의 번호
    chks = []  # 각 치킨집의 좌표 저장. 인덱스 = 각 치킨 집의 번호
    for r in range(N):
        row = list(map(int, input().split()))
        for c, v in enumerate(row):
            if v == 1:
                houses.append((r, c))
            elif v == 2:
                chks.append((r, c))
        city.append(row)

    # 초기 치킨 거리 탐색
    clst_chk = [None] * len(houses)
    chk_cstm = [0] * len(chks)
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)] # 집을 중심으로 12시 방향부터 시계 방향으로 9칸
    for h, h_pos in enumerate(houses):
        hr, hc = h_pos
        offset = 0
        min_dist = 2 * N
        for dr, dc in dir:
            if hr+dr < N and hc+dc < N and city[hr+dr][hc+dc] == 2:
                curr_dist = offset+abs(dr+dc)
                if curr_dist < min_dist:
                    chk = chks.index((hr+dr, hc+dc))
                    clst_chk[h] = (chk, curr_dist)
                    chk_cstm[chk] += 1
            if clst_chk[h]:
                break

            offset += 1

    ans = ''


solution()
