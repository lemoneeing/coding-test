import sys
input = sys.stdin.readline

def solution1():
    '''
    각 집과 치킨집의 좌표를 각각 리스트(houses, chks)로 정리
    1) 집을 기준으로 탐색하여
       각 집의 (최단치킨집,치킨거리)를 리스트(clst_chk - 이때 인덱스는 집의 번호 의미)로
       각 치킨집의 고객수를 리스트로(chk_cstm - 이때 인덱스는 치킨집 번호 의미)로 정리
    2) chk_cstm 값이 작은 치킨집부터 제거: city 좌표에서 2 -> 0
    3) 집을 기준으로 재탐색
    => 시간초과 난다함.
    :return:
    '''
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
    for h, (hr, hc) in enumerate(houses):

        offset = 0
        min_dist = 2 * N
        while not clst_chk[h]:
            for dr, dc in dir:
                tr = hr+(dr*(offset+1))
                tc = hc+(dc*(offset+1))
                if 0 <= tr < N and 0 <= tc < N and city[tr][tc] == 2:
                    curr_dist = offset+abs(dr+dc)
                    if curr_dist < min_dist:
                        chk = chks.index((tr, tc))
                        clst_chk[h] = (chk, curr_dist)
                        chk_cstm[chk] += 1
            offset += 1

def solution():

    N, M = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(N)]
    houses = [(r, c) for c in range(N) for r in range(N) if city[r][c] == 1]
    chks = [(r, c) for c in range(N) for r in range(N) if city[r][c] == 2]

    selected = [False] * len(chks)
    min_total = sys.maxsize
    def calculate_distance():
        nonlocal houses, chks
        total = 0
        for hr, hc in houses:
            min_dist = 2 * N
            for i, (cr, cc) in enumerate(chks):
                if selected[i]:
                    min_dist = min(min_dist, abs(hr-cr) + abs(hc-cc))
            total += min_dist

        return total
    def select_m_chickens(start, cnt):
        nonlocal M, chks, selected, min_total

        if cnt == M:
            return min(min_total, calculate_distance())

        for i in range(start, len(chks)):
            selected[i] = True
            min_total = select_m_chickens(i+1, cnt+1)
            selected[i] = False

        return min_total

    sys.stdout.write(f"{select_m_chickens(0, 0)}")

solution()
