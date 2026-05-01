import sys
from collections import deque
input = sys.stdin.readline

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def add_morning_belief(SIZE, B):
    # 아침: 모두의 신앙심 1 증가
    for r in range(SIZE):
        for c in range(SIZE):
            B[r][c] += 1


def set_noon_group(SIZE, F, B):
    # 점심: 동일 음식끼리 그룹 형성, 대표 선정
    G = [[] for _ in range(SIZE**2)] # 각 그룹 별 학생 좌표 저장, 인덱스 = 음식을 정수(gid)로 치환한 값
    # G = {'T':[], 'C':[], 'M':[], 'CM':[], 'MT': [], 'CT':[], 'CMT':[]}
    # FG = {'T':[], 'C':[], 'M':[], 'CM':[], 'MT': [], 'CT':[], 'CMT':[]} # 각 음식을 신봉하는 그룹 넘버 리스트
    FG = [-1] * (SIZE**2)
    
    # 그룹 형성 (BFS)
    gid = 0
    visited = [[False] * SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        for c in range(SIZE):
            if not visited[r][c]: # 그룹 미형성 구간만 탐색
                visited[r][c] = True
                q = deque([(r, c)])
                FG[gid] = F[r][c]
                G[gid].append((r, c))
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in DIR:
                        mr = cr + dr
                        mc = cc + dc
                        if 0 <= mr < SIZE and 0 <= mc < SIZE and not visited[mr][mc] and F[mr][mc] == F[r][c]:
                            G[gid].append((mr, mc))
                            q.append((mr, mc))
                            visited[mr][mc] = True
                gid += 1

    # 대표 
    H = [[] for _ in range(gid)]
    for g in range(gid):
        max_b = 0
        min_r = SIZE
        min_c = SIZE

        # 인덱스 g 에 해당하는 음식 별 그룹을 탐색
        for gr, gc in G[g]:
            if max_b < B[gr][gc]:
                max_b = B[gr][gc]
                min_r = gr
                min_c = gc
                H[g] = (gr, gc)
            elif max_b == B[gr][gc]:
                if min_r > gr:
                    min_r = gr
                    min_c = gc
                    H[g] = (gr, gc)
                elif min_r == gr:
                    if min_c > gc:
                        min_c = gc
                        H[g] = (gr, gc)

        # 신앙심 재분배: 대표 제외 1씩 감소
        for ggr, ggc in G[g]:
            if (ggr, ggc) == H[g]:
                B[ggr][ggc] += (len(G[g]) - 1)
            else:
                B[ggr][ggc] -= 1

    return G, H, FG

def spread_foot_at_dinner(SIZE, F, B, H, FG):
    # 단일(민트/초코/우유) - 이중(초코우유/민트우유/민트초코) - 다중(민트초코우유) 순으로 탐색

    # 전파 순서 결정
    food_orders = [[] for _ in range(4)] # food_orders[1]: 1글자짜리 음식의 전파 순서

    for gid, curr_h_pos in enumerate(H):
        ft = FG[gid]
        chr, chc = curr_h_pos
        group_type = len(ft)
        if len(food_orders[group_type]) == 0:
            food_orders[group_type].append(gid)
        else:
            chr, chc = H[gid] # 현재 확인하려는 음식그룹의 대표 curr head row/col
            thr, thc = H[food_orders[group_type][0]] # 비교하려는 음식그룹 대표 target head row/col
            if B[chr][chc] > B[thr][thc] or (B[chr][chc] == B[thr][thc] and (chr < thr or (chr == thr and chc < thc))):
                food_orders[group_type].insert(0, gid)
                continue
            else:
                if len(food_orders[group_type]) > 1: # 비교할 음식그룹이 더 있으면
                    sthr, sthc = H[food_orders[group_type][1]]
                    if B[chr][chc] > B[sthr][sthc] or (B[chr][chc] == B[sthr][sthc] and (chr < sthr or (chr == sthr and chc < sthc))):
                        food_orders[group_type].insert(1, gid)
                        continue
                
            food_orders[group_type].append(gid)

    # 전파
    is_defensive = [[False] * SIZE for _ in range(SIZE)]
    for fo in food_orders[1:]:
        for curr_g in fo:
            cr, cc = H[curr_g]
            if is_defensive[cr][cc]: # 방어상태 = 전파 불가능
                continue

            dr, dc = DIR[B[cr][cc] % 4]
            eager = B[cr][cc] - 1
            B[cr][cc] = 1

            tr = cr
            tc = cc
            while eager > 0:
                tr += dr
                tc += dc
                if (tr < 0 or SIZE <= tr) or (tc < 0 or SIZE <= tc ):
                    break

                # if (len(F[tr][tc]) == len(F[cr][cc]) and F[tr][tc] != F[cr][cc]) or (len(F[tr][tc]) > len(F[cr][cc]) and F[cr][cc] not in F[tr][tc]) or (len(F[tr][tc]) < len(F[cr][cc]) and F[tr][tc] not in F[cr][cc]):
                if F[tr][tc] != F[cr][cc]:
                    if B[tr][tc] < eager: # 강한전파
                        B[tr][tc] += 1
                        eager -= B[tr][tc]
                        F[tr][tc] = FG[curr_g]
                    else:                      # 약한전파
                        B[tr][tc] += eager
                        eager = 0
                        # if FG[curr_g] not in F[tr][tc] and F[tr][tc] not in FG[curr_g]:
                        #     F[tr][tc] = ''.join(sorted(f"{FG[curr_g] + F[tr][tc]}"))
                        F[tr][tc] = FG[curr_g] | F[tr][tc]
                        
                    is_defensive[tr][tc] = True

def solve():
    N, T = map(int, input().strip().split())
    F = [[set(e) for e in list(input().strip())] for _ in range(N)]
    # F = [list(input().strip()) for _ in range(N)] # 신봉음식
    B = [list(map(int, input().split())) for _ in range(N)] # 신앙심

    for _ in range(T):
        add_morning_belief(N, B)
        G, H, FG = set_noon_group(N, F, B)
        # print(H)
        # print(B)
        # print(FG)

        spread_foot_at_dinner(N, F, B, H, FG)
        # print(F)
        # print(B)

        sum_belief = {'CMT':0, 'CT':0, 'MT':0, 'CM':0, 'M':0, 'C':0, 'T':0}
        for r in range(N):
            for c in range(N):
                key = "".join(sorted(list(F[r][c])))
                if key in sum_belief:
                    sum_belief[key] += B[r][c]
          
        sys.stdout.write(f"{' '.join(map(str, sum_belief.values()))}\n")

solve()


import sys
from collections import deque

input = sys.stdin.readline

# 위, 아래, 왼쪽, 오른쪽 방향 정의
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def add_morning_belief(SIZE, B):
    """아침: 모든 학생의 신앙심 1 증가"""
    for r in range(SIZE):
        for c in range(SIZE):
            B[r][c] += 1

def set_noon_group(SIZE, F, B):
    """점심: 동일 음식끼리 그룹 형성 및 대표 선정, 신앙심 재분배"""
    visited = [[False] * SIZE for _ in range(SIZE)]
    groups = [] # (그룹 좌표 리스트, 그룹 음식 set) 저장
    
    for r in range(SIZE):
        for c in range(SIZE):
            if not visited[r][c]:
                curr_f = F[r][c]
                q = deque([(r, c)])
                visited[r][c] = True
                group_coords = [(r, c)]
                
                while q:
                    cr, cc = q.popleft()
                    for dr, dc in DIR:
                        mr = cr + dr
                        mc = cc + dc
                        # 음식이 '완전히' 같은 경우만 그룹화 (set 비교)
                        if 0 <= mr < SIZE and 0 <= mc < SIZE and not visited[mr][mc] and F[mr][mc] == curr_f:
                            visited[mr][mc] = True
                            group_coords.append((mr, mc))
                            q.append((mr, mc))
                groups.append((group_coords, curr_f))

    group_info = [] # 전파 단계에서 사용할 대표 정보 저장
    for group_coords, food_set in groups:
        # 대표 선정 기준: 1. 신앙심 큰 순 2. 행 작은 순 3. 열 작은 순
        # sort의 key를 사용해 한 번에 정렬
        group_coords.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
        head_r, head_c = group_coords[0]
        
        # 신앙심 재분배: 대표는 (원래수-1)만큼 얻고, 나머지는 1씩 감소
        transfer_amount = len(group_coords) - 1
        for gr, gc in group_coords:
            if (gr, gc) == (head_r, head_c):
                B[gr][gc] += transfer_amount
            else:
                B[gr][gc] -= 1
        
        group_info.append({'head': (head_r, head_c), 'food': food_set})
        
    return group_info

def spread_foot_at_dinner(SIZE, F, B, group_info):
    """저녁: 단계별 전파 진행"""
    # 1. 전파 순서 결정용 리스트 생성
    # 정렬 기준: 1. 음식 종류 수 2. 대표 신앙심 높은 순 3. 행 작은 순 4. 열 작은 순
    group_info.sort(key=lambda x: (
        len(x['food']), 
        -B[x['head'][0]][x['head'][1]], 
        x['head'][0], 
        x['head'][1]
    ))

    is_defensive = [[False] * SIZE for _ in range(SIZE)]
    
    for g in group_info:
        hr, hc = g['head']
        
        # 방어 상태 확인: 당일 이미 전파를 받은 대표는 전파하지 않음
        if is_defensive[hr][hc]:
            continue
            
        eager = B[hr][hc] - 1
        direction_idx = B[hr][hc] % 4
        dr, dc = DIR[direction_idx]
        B[hr][hc] = 1 # 전파자는 신앙심 1만 남음
        
        curr_food = g['food']
        tr, tc = hr, hc
        
        while eager > 0:
            tr += dr
            tc += dc
            
            # 격자 밖으로 나가면 종료
            if not (0 <= tr < SIZE and 0 <= tc < SIZE):
                break
            
            # 대상과 음식이 완전히 같으면 전파 없이 다음 칸으로 이동
            if F[tr][tc] == curr_food:
                continue
            
            # 전파 발생 (전파 받은 대상은 즉시 방어상태)
            is_defensive[tr][tc] = True
            y = B[tr][tc]
            
            if eager > y: # 강한 전파
                B[tr][tc] += 1
                eager -= (y + 1)
                F[tr][tc] = set(curr_food) # 완전히 동화
                if eager == 0: break
            else: # 약한 전파
                B[tr][tc] += eager
                F[tr][tc] = F[tr][tc] | curr_food # 기본 음식들 합침
                eager = 0 # 간절함 소진되어 종료

def solve():
    input_data = input().split()
    if not input_data: return
    N, T = map(int, input_data)
    
    # 초기 음식 상태 (set으로 저장)
    F = [[set(char) for char in input().strip()] for _ in range(N)]
    # 초기 신앙심
    B = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(T):
        add_morning_belief(N, B)
        group_info = set_noon_group(N, F, B)
        spread_foot_at_dinner(N, F, B, group_info)

        # 결과 출력을 위한 음식 순서 정의
        order = ['CMT', 'CT', 'MT', 'CM', 'M', 'C', 'T']
        sum_belief = {k: 0 for k in order}
        
        for r in range(N):
            for c in range(N):
                key = "".join(sorted(list(F[r][c])))
                if key in sum_belief:
                    sum_belief[key] += B[r][c]
        
        # 순서대로 출력
        print(*(sum_belief[k] for k in order))

if __name__ == "__main__":
    solve()