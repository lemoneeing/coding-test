import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    farm = [[0]*N for _ in range(N)]
    f_types = [0]
    for _ in range(M):
        x, y, l, f = map(int, input().split())
        for r in range(y, y+l):
            for c in range(x, x+l):
                farm[r][c] = f
                f_types.append(f)

    # 각 과일 별 + 영역 별 누적 합
    prefix_fruits = [[[0] * N for __ in range(N)] for _ in range(8)]
    prefix_fruits[farm[0][0]][0][0] += 1 # (0, 0) 에 위치한 과일의 누적 합을 1로 초기화
    for f_type in f_types:
        for r in range(1, N):
            for c in range(1, N):
                add_cnt = 1 if farm[r][c] == f_type else 0
                prefix_fruits[f_type][r][c] = (prefix_fruits[f_type][r-1][c] +    # (0,0) ~ (r-1, c-1) 까지의 과일 누적 합
                                               prefix_fruits[f_type][r][c-1] -          # (0, c) ~ (r, c) 의 과일 개수 합
                                               prefix_fruits[f_type][r-1][c-1] +
                                               add_cnt)           # (c, 0) ~ (c, r) 의 과일 개수 합

    ans = ''


solution()
