import sys
from itertools import combinations

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 1. 펜타 모듈 생성(백트래킹)
    all_penta = []
    temp_penta_sets = []

    def find_all_penta(current_set):
        if len(current_set) == 5:
            s_set = set(current_set)
            if s_set not in temp_penta_sets:
                temp_penta_sets.append(s_set)
                total = sum(grid[r][c] for r, c in s_set)
                all_penta.append({'cells': s_set, 'sum': total})
            return

        for r, c in list(current_set):
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in current_set:
                    current_set.add((nr, nc))
                    find_all_penta(current_set)
                    current_set.remove((nr, nc))

    for r in range(N):
        for c in range(M):
            find_all_penta({(r, c)})

    # 2. 두 모듈의 조합 중 '정확히 2개'가 겹치는 경우 탐색
    max_efficiency = -float('inf')
    
    # 생성된 모든 펜타 모듈 중 2개를 선택 (조합)
    for i in range(len(all_penta)):
        for j in range(i + 1, len(all_penta)):
            m1 = all_penta[i]
            m2 = all_penta[j]
            
            # 교집합(겹치는 셀) 계산
            overlap = m1['cells'].intersection(m2['cells'])
            
            if len(overlap) == 2:
                # 점수 계산: (모듈1 합 + 모듈2 합) 
                # -> 겹친 부분은 m1에서 한 번, m2에서 한 번 더해졌으므로 이미 2배가 됨
                current_score = m1['sum'] + m2['sum']
                if current_score > max_efficiency:
                    max_efficiency = current_score

    print(max_efficiency)

solve()