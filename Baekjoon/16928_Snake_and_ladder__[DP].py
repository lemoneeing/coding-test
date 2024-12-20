import math
import sys
from heapq import heappush

input = sys.stdin.readline

def solution():
    L, S = map(int, input().split())
    snakes = {}
    ladders = {}

    for l in range(L):
        num_pair = tuple(map(int, input().split()))
        ladders[num_pair[0]] = num_pair[1]

    for s in range(S):
        num_pair = tuple(map(int, input().split()))
        snakes[num_pair[0]] = num_pair[1]

    # 뱀이나 사다리 없을 경우 이동 횟수
    q = [1]
    board = [1] * 101
    visited = [False] * 101
    while q:
        curr = q.pop(0)
        if curr == 100:
            break

        for i in range(1, 7):
            next = curr+i
            if next <= 100 and not visited[next]:
                if next in ladders.keys():
                    next = ladders[next]

                if next in snakes.keys():
                    next = snakes[next]

                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    board[next] = board[curr] + 1

    print(board[100])

solution()