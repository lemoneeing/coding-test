import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    wood = [list(map(int, input().split())) for _ in range(N)]

    if N * M < 3:
        print(0)
        return

    visited = [[False] * M for _ in range(N)]
    boomerang_formats = [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(0, 1), (1, 0)]]
    ans = 0

    def make_boomerang(r, c, strength):
        nonlocal N, M, wood, boomerang_formats, visited, ans

        if c == M:
            make_boomerang(r+1, 0, strength)
            return
        
        if r == N:
            ans = max(ans, strength)
            return

        # r, c 를 중심으로 부메랑 제작
        if not visited[r][c]:

            for form in boomerang_formats:
                hr, hc = r + form[0][0], c+ form[0][1]
                tr, tc = r + form[1][0], c+ form[1][1]

                if 0 <= hr < N and 0 <= hc < M and not visited[hr][hc] and 0 <= tr < N and 0 <= tc < M and not visited[tr][tc]:
                    visited[hr][hc] = visited[r][c] = visited[tr][tc] = True
                    make_boomerang(r, c+1, strength + (wood[hr][hc] + wood[r][c] * 2 + wood[tr][tc]))
                    visited[hr][hc] = visited[r][c] = visited[tr][tc] = False
        
        make_boomerang(r, c+1, strength)
        
    make_boomerang(0, 0, 0)

    print(ans)

solve()