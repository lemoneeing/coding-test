import sys
input = sys.stdin.readline


def solution():
    R, C = map(int, input().split())
    woods = []
    hedgehog = None
    beaver = None
    water = []
    for i in range(R):
        line = []
        for j, letter in enumerate(input().strip()):
            if letter == 'S':
                hedgehog = (i, j)
            elif letter == 'D':
                beaver = (i, j)
            elif letter == '*':
                water.append((i, j))
            line.append(letter)
        woods.append(line)

    q = [hedgehog]
    q.extend(water)
    visited = [[0] * C for _ in range(R)]
    while q:
        r, c = q.pop(0)
        if woods[r][c] == 'D':
            break

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if woods[r][c] == 'S':
                    if woods[nr][nc] in ('.', 'D'):
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1
                        if woods[nr][nc] == '.':
                            woods[nr][nc] = woods[r][c]

                elif woods[r][c] == '*':
                    if woods[nr][nc] in ('.', 'S'):
                        woods[nr][nc] = woods[r][c]
                        visited[nr][nc] = 0
                        if (nr, nc) not in q:
                            q.append((nr, nc))

    br, bc = beaver
    if visited[br][bc] > 0:
        print(visited[br][bc])
    else:
        print('KAKTUS')

solution()
