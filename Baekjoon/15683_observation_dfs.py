import sys

N, M = map(int, sys.stdin.readline().split())
room = [[6] * (M + 1)] + [[6] + list(map(int, sys.stdin.readline().split())) + [6] for _ in range(N)] + [[6] * (M + 1)]

# 방향 좌표(상, 우, 하, 좌) dPos = [(0, -1), (1, 0), (0, 1), (1, 0)]
# cctv type 별 감시 방향 인덱스 [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]
# cctv[1] = 1번 유형 cctv 의 감시 방향 인덱스 배열
# (반복)
#   dPos[cctv[1][0]] = (1, 0) 을 현재 cctv 좌표에 더함  -> ci, cj
#   if room[ci][cj] == 6: break
#   else: visited[ci][cj] = True

# cctv 한 대에 대해 모든 방향 확인
# 필요한 것: cctv 현재 위치 cctv 유형, 감시 방향 인덱스, 감시 방향 좌표,
dPos = [(0, -1), (1, 0), (0, 1), (1, 0)] # 감시 방향 4 종류를 좌표로 표현
cctv = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]] # 각 cctv 별 감시 방향의 인덱스


def observe(row, col):
    if type(room[row][col]) is str or room[row][col] < 1 or room[row][col] > 5:
        return

    dIdxArr = cctv[room[row][col]]  # 감시 방향 인덱스
    # 감시해야하는 방향으로 쭉 감시
    for i in dIdxArr:
        while room[row][col] != 6:
            room[row][col] = '#'
            row += dPos[i][0]
            col += dPos[i][1]

for x in range(1, N+1):
    for y in range(1, M+1):
        observe(x, y)

for x in range(1, N+1):
    print(room[x][1:-1])