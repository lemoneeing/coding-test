import sys
input = sys.stdin.readline

def add_morning_belief(SIZE, B):
    # 아침: 모두의 신앙심 1 증가
    for r in SIZE:
        for c in SIZE:
            B[r][c] += 1


def set_noon_group(SIZE, F, B):
    # 점심: 동일 음식끼리 그룹 형성, 대표 선정 (BFS)
    G = [[] for _ in range(SIZE+1)] # 각 그룹에 속하는 학생 좌표 저장
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 그룹 형성
    gid = 1
    visited = [[False] * SIZE for _ in range(SIZE)]
    for r in range(SIZE):
        for c in range(SIZE):
            curr_f = F[r][c]
            if not visited[r][c]: # 그룹 미형성 구간만 탐색
                q = [(r, c)]
                visited[r][c] = True
                G[gid].append((r, c))
                while q:
                    cr, cc = q.pop(0)
                    for dr, dc in dir:
                        mr = cr + dr
                        mc = cc + dc
                        if 0 <= mr < SIZE and 0 <= mc < SIZE and not visited[mr][mc] and F[mr][mc] == curr_f:
                            G[gid].append((mr, mc))
                            q.append((mr, mc))
                            visited[mr][mc] = True
                gid += 1

    # 대표 선정
    H = [None] * gid # 각 그룹 별 대표
    for g in range(1, gid):
        max_b = 0
        min_r = SIZE
        min_c = SIZE
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

        for ggr, ggc in G[g]:
            if (ggr, ggc) == H[g]:
                B[ggr][ggc] += (len(G[g]) - 1)
            else:
                B[ggr][ggc] -= 1

    return G, H
def solution():
    N, T = map(int, input().strip().split())
    F = [list(input().strip()) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(N)]

    G, H = set_noon_group(N, F, B)
    print(G)
    print(H)
    print(B)



    '''
    
    
    
    점심
    
    저녁
    '''

solution()
