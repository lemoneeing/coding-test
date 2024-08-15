import sys

class Token:
    dir = [(0,0), (1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, x, y, d):
        self.x = 0
        self.y = 0
        self.d = 0

    def turn(self):
        return self.x + self.dir[self.d][0], self.y + self.dir[self.d][1]


def solution():
    N, K = map(int, sys.stdin.readline().split())
    visited = [[False] * (N+2) for _ in range(N+2)]
    board = [[2] * (N+2)]
    tokens = []

    print(visited)


    for _ in range(N):
        board.append([2])
        board[-1].extend(list(map(int, sys.stdin.readline().split())))
        board[-1].append(2)
    board.append([2]*(N+2))

    for k in range(K):
        r, c, d = map(int, sys.stdin.readline().split())
        tokens.append(Token(r, c, d))


    while True:
        for token in tokens:
            token.turn()




solution()