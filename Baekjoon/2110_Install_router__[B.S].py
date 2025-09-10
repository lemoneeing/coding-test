import sys
input = sys.stdin.readline
# def solution():
#     H, R = map(int, input().strip().split())
#     houses = []
#     for _ in range(H):
#         houses.append(int(input().strip()))
#     houses.sort()
#
#     # 1. 공유기를 최대한 멀리 설치
#     #   멀리 설치하려면?
#
#     # 2. 그 중 가장 가까운 거리는?
#     installed = []
#     adj = []
#     longest = 0
#     def install(idx, installable):
#         nonlocal R, houses, installed, longest
#
#         if len(installed) == R:
#             return
#
#         if installable:
#             if installed:
#                 currDist = abs(installed[-1] - houses[idx])
#                 if currDist > longest:
#                     longest = currDist
#
#             installed.append(houses[idx])
#
#         return max(install(idx + 1, True), install(idx + 1, False)))
#
#     for h in houses:
#         install(h)
#         install()

# ### 남의 풀이
# N, C = map(int, input().split())
#
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
# arr.sort()
#
# start = 1 # 공유기 거리 최소
# end = arr[-1] - arr[0] # 공유기 거리 최대
# result = 0
#
# # 재귀로 적절한 두 공유기 사이의 거리를 찾는다
# while (start <= end):
#     mid = (start + end) // 2 # 현재 공유기 거리
#     current = arr[0]
#     count = 1
#
#     # 공유기 설치 몇 대 할 수 있는지 체크
#     for i in range(1, len(arr)):
#         if arr[i] >= current + mid:
#             count += 1
#             current = arr[i]
#     # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
#     if count >= C:
#         start = mid + 1
#         result = mid
#     # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
#     else:
#         end = mid - 1
#
# print(result)
#

# 순열, 백트래킹 -> 시간초과
# sys.setrecursionlimit(1000000)
# def solution():
#
#     N, C = map(int, input().split())
#     houses = []
#     for _ in range(N):
#         houses.append(int(input()))
#     houses.sort()
#
#     max_adj = 0
#     adj = houses[-1] - houses[0]
#     def pick_houses(pick, h):
#         nonlocal N, C, houses, max_adj
#
#         # 최단 인접 거리 구하기
#         if len(pick) == C:
#             adj = sys.maxsize
#             for i in range(C - 1):
#                 dist = pick[i + 1] - pick[i]
#                 adj = min(adj, dist)
#             return adj
#
#         # C 만큼의 집 고르기
#         if h < N:
#             if houses[h] not in pick:
#                 pick.append(houses[h])
#                 max_adj = max(max_adj, pick_houses(pick, h + 1))
#                 pick.remove(houses[h])
#
#             max_adj = max(max_adj, pick_houses(pick, h + 1))
#
#         return max_adj
#
#     sys.stdout.write(f"{pick_houses([], 0)}")
#
# solution()

# 이분 탐색
def solution():
    N, C = map(int, input().split())
    houses = [int(input()) for _ in range(N)]
    houses.sort()

    long = 0
    shortest = 1  # 인접 거리 중 최단
    longest = houses[-1] - houses[0]  # 인접 거리 중 최장

    # 인접 거리가 될 수 있는 길이 내에서 탐색
    while shortest <= longest:
        mid = (shortest + longest) // 2
        curr = houses[0]
        installed = 1

        for h in houses[1:]:
            # mid 만큼 띄워 설치할 수 있는 집의 수 카운트
            if curr + mid <= h:
                installed += 1
                curr = h

        # 목표 설치 개수 미달 -> 임의의 최단 인접 거리 감소
        if installed < C:
            longest = mid - 1

        # 목표 설치 개수 초과 -> 임의의 최단 인접 거리 증가
        if installed >= C:
            shortest = mid + 1
            long = max(long, mid)  # 목표 설치 개수를 달성하긴 했으므로 최장 거리 갱신

    sys.stdout.write(f"{long}")

solution()