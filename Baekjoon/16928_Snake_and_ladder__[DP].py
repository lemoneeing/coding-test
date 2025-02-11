## 맞는 풀이
import sys
input = sys.stdin.readline

def solution():
    # 입력
    L, S = map(int, input().split())

    ladders = {}
    for _ in range(L):
        s, e = map(int, input().split())
        ladders[s] = e

    snakes = {}
    for _ in range(S):
        s, e = map(int, input().split())
        snakes[s] = e


    # 방식: 현재 칸 + 6까지 BFS 탐색 (다음 이동할 칸이 사다린지, 뱀인지 확인)
    bfs = [[1], []]
    visited = [False] * 101
    visited[1] = True
    cnt = 0

    while bfs:
        curr_pts = bfs.pop(0)
        for curr_pt in curr_pts:
            for i in range(1, 7):
                next_pt = curr_pt + i

                if next_pt in ladders:
                    next_pt = ladders[next_pt]

                elif next_pt in snakes:
                    next_pt = snakes[next_pt]

                if not visited[next_pt]:
                    visited[next_pt] = True
                    if next_pt == 100:
                        sys.stdout.write(f"{cnt+1}")
                        return
                    else:
                        bfs[-1].append(next_pt)
        cnt += 1
        bfs.append([])

solution()

## 틀린 풀이
# import sys
# from heapq import heappush
#
# input = sys.stdin.readline
#
# def solution():
#     L, S = map(int, input().split())
#     snakes = {}
#     ladders = {}
#
#     for l in range(L):
#         num_pair = tuple(map(int, input().split()))
#         ladders[num_pair[0]] = num_pair[1]
#
#     for s in range(S):
#         num_pair = tuple(map(int, input().split()))
#         snakes[num_pair[0]] = num_pair[1]
#
#     # 뱀이나 사다리 없을 경우 이동 횟수
#     q = [1]
#     board = [1] * 101
#     visited = [False] * 101
#     while q:
#         curr = q.pop(0)
#         if curr == 100:
#             break
#
#         for i in range(1, 7):
#             next = curr+i
#             if next <= 100 and not visited[next]:
#                 if next in ladders.keys():
#                     next = ladders[next]
#
#                 if next in snakes.keys():
#                     next = snakes[next]
#
#                 if not visited[next]:
#                     q.append(next)
#                     visited[next] = True
#                     board[next] = board[curr] + 1
#
#     print(board[100])
#
# solution()