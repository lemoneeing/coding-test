import math
import sys
from heapq import heappush

input = sys.stdin.readline

def solution():
    L, S = map(int, input().split())
    path = []
    snakes = {}
    ladders = {}

    for l in range(L):
        num_pair = tuple(map(int, input().split()))
        path.append(num_pair)
        ladders[num_pair[0]] = num_pair[1]

    for s in range(S):
        num_pair = tuple(map(int, input().split()))
        path.append(num_pair)
        snakes[num_pair[0]] = num_pair[1]

    # 뱀이나 사다리 없을 경우 이동 횟수
    board = [0] * 101
    w = 1
    for i in range(1, 101, 6):
        board[i:i+6] = [w] * 6
        w += 1

    q = [i for i in range(1, 7)]
    while q:
        curr = q.pop(0)

    print(board[100])

solution()