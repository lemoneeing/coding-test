import sys

input = sys.stdin.readline
R, C = map(int, input().strip().split())
GRID = [list(input().strip()) for _ in range(R)]
ans = 0

def dfs(r, c, level, visited_alphabets):
    global ans

    ans = max(ans, level)

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc

        if 0<= nr < R and 0 <= nc < C:
            nxt = ord(GRID[nr][nc]) - ord('A')
            
            if not visited_alphabets[nxt]:
                visited_alphabets[nxt] = True
                dfs(nr, nc, level+1, visited_alphabets)
                visited_alphabets[nxt] = False


def solve():
    global R, C, GRID

    visited = [False] * 26
    visited[ord(GRID[0][0]) - ord('A')] = True
    dfs(0, 0, 1, visited)

    print(ans)

solve()