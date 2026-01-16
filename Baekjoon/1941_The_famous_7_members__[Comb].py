from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

LIMIT = 5
def main():
    classroom = []
    for _ in range(LIMIT):
        classroom.append(input().strip())
    
    '''
    25명 (5x5)
    입력)  ->  출력) 2
    YYYYY     .....    .....
    SYSYS     SYSYS    SYSYS
    YYYYY     ....Y    .Y...
    YSYYS     ....S    .S...
    YYYYY     .....    .....

    조합 + BFS
     0  1  2  3  4
     5  6  7  8  9 
    10 11 12 13 14
    15 16 17 18 19
    20 21 22 23 24
    '''

    combs = combinations(range(LIMIT * LIMIT), 7)

    ans = 0
    for comb in combs:
        if is_7_neighbors(classroom, comb):
            ans += 1
    
    print(ans)


def is_7_neighbors(classroom, comb):

    s_cnt = 0
    visited = set()
    visited.add(comb[0])
    q = deque([comb[0]])
    comb_set = set(comb)

    while q:
        pos = q.popleft()
        r, c = pos // LIMIT, pos % LIMIT       

        # S >= 4
        if classroom[r][c] == 'S':
            s_cnt += 1
        
        # 서로 다 인접인지
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            adjr = r + dr
            adjc = c + dc
            if 0 <= adjr < LIMIT and 0<= adjc < LIMIT:
                adj_pos = adjr * 5 + adjc

                if adj_pos in comb_set and adj_pos not in visited:
                    visited.add(adj_pos)
                    q.append(adj_pos)
                                 

    if s_cnt >= 4 and len(visited) == 7:
        return True
    else:
        return False
    
main()