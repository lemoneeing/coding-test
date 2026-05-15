class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0]*m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        q = []
        for r, c, cl in sources:
            grid[r][c] = (0, cl)
            visited[r][c] = True
            q.append((r, c))
            
        # BFS 탐색
        lev = 1
        while q:
            for _ in range(len(q)):
                cr, cc = q.pop(0)
                # if grid[cr][cc] < 0:
                    # grid[cr][cc] = -grid[cr][cc]

                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr = cr + dr
                    nc = cc + dc

                    # 탐색 종료 조건: 인접한 네 칸이 모두 0이 아닐 때
                    if 0 <= nr < n and 0 <= nc < m and (grid[nr][nc] == 0 or grid[nr][nc][0] == lev): # and not visited[nr][nc]
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = (lev, grid[cr][cc][1])
                            q.append((nr, nc))
                        elif grid[nr][nc][1] != grid[cr][cc][1]:
                            grid[nr][nc] = (lev, grid[nr][nc][1]) if grid[nr][nc][1] > grid[cr][cc][1] else (lev, grid[cr][cc][1])
            lev += 1
        

        for r in range(n):
            for c in range(m):
                grid[r][c] = grid[r][c][1]

        return grid


def solve(n, m, args):

    solution = Solution()

    
    for row in solution.colorGrid(n, m, args):
        print(row)



solve(3, 3, [[0,0,1],[2,2,2]]) # [[1,1,2],[1,2,2],[2,2,2]]
# solve(3, 3, [[0,1,3],[1,1,5]]) # [[3,3,3],[5,5,5],[5,5,5]]
# solve(2, 3, [[0,2,926647],[1,0,485097]]) # [[485097,926647,926647],[485097,485097,926647]]
