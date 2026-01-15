import sys
input = sys.stdin.readline

LIMIT = 5
def main():
    room = []
    for _ in range(LIMIT):
        room.append(input().split())
    
    '''
    25명 (5x5)
    입력)  ->  출력) 2
    YYYYY     .....    .....
    SYSYS     SYSYS    SYSYS
    YYYYY     ....Y    .Y...
    YSYYS     ....S    .S...
    YYYYY     .....    .....


    BFS

    1. 전체 순회 grid
        curr_start = grd
        q = [curr_start]
        길이 = 1
        y_cnt = 1 if grid[curr_start] == Y else 0
        while q:
            next_cnt = len(q)
            for curr in q[:next_cnt]:
                grid[curr] = 길이
                for next in 4방면
                    if Y >= 4 AND 길이 > 7:
                        끝. 더 탐색 X
                    else
                        if next == Y:
                            Y += 1
                        q.append(next)
            길이 += 1

    '''
    ans = 9
    for r in range(LIMIT):
        for c in range(LIMIT):
            start = (r, c)
            q = [start]
            member_note = [[(0, 0) for __ in range(LIMIT)] for _ in range(LIMIT)]
            member_note[r][c] = (1, 1 if room[r][c] == 'Y' else 0)
            while q:
                qq = q[:len(q)]
                while qq:
                    cr, cc = qq.pop(0)
                    curr_mem = member_note[cr][cc]
                    
                    if curr_mem[0] > 7 or curr_mem[1] > 3:
                        continue


                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nr = cr + dr
                        nc = cc + dc

                        if 0 <= nr < LIMIT and 0 <= nc < LIMIT:
                            next_len = curr_mem[0] + 1
                            y_cnt = curr_mem[1] + 1 if room[nr][nc]  == 'Y' else curr_mem[1]

                            if next_len <= 7 and y_cnt <= 3:
                                if next_len == 7:
                                    ans += 1

                                else:
                                    member_note[nr][nc] = (next_len, y_cnt)
                                    q.qppend((nr, nc))
    
main()