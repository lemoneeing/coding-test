import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    tetrominos = [((0, 1), (0, 1), (0, 1)),  # ㅡ
                  ((0, 1), (1, 0), (0, -1)), # ㅁ
                  ((1, 0), (1, 0), (0, 1)),  # ㄴ
                  ((1, 0), (0, 1), (1, 0)),  # ㄹ
                  (0, 1), (0, 1), (1, -1)]   #  ㅜ



    ans = ''


solution()
