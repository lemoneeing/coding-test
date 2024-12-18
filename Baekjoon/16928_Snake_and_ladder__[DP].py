import math
import sys
from heapq import heappush

input = sys.stdin.readline

def solution():
    L, S = map(int, input().split())
    path = []
    snakes = []
    ladders = []
    for _ in range(L):
        num_pair = tuple(map(int, input().split()))
        heappush(path, num_pair)
        heappush(ladders, num_pair)

    for _ in range(S):
        num_pair = tuple(map(int, input().split()))
        heappush(path, num_pair)
        heappush(snakes, num_pair)

    # 기본
    board = [0] * 101
    for i in range(101):
        if i < 6:
            board[i] = i % 6
        else:
            board[i] = math.ceil(i / 6)

    # 사다리
    for ladder in ladders:
        board[ladder[1]] = min(board[ladder[1]], board[ladder[0]])

    # 사디리로 도달 횟수가 갱신된 칸을 기준으로 다음 칸의 도달 횟수를 +1 씩하여 갱신 -> 100번

    # 뱀

    # 뱀으로 갱신된 칸 기준으로 다음 칸 도달 횟수 갱신 -> 100

    dp = []
    print(path)
    print(ladders)
    print(snakes)

solution()