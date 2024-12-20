# import sys
#
# input = sys.stdin.readline
#
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

### 남의 풀이
N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

start = 1 # 공유기 거리 최소
end = arr[-1] - arr[0] # 공유기 거리 최대
result = 0

# 재귀로 적절한 두 공유기 사이의 거리를 찾는다
while (start <= end):
    mid = (start + end) // 2 # 현재 공유기 거리
    current = arr[0]
    count = 1

    # 공유기 설치 몇 대 할 수 있는지 체크
    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]
    # 공유기 설치 수가 목표 보다 크면 공유기 사이 거리 늘림
    if count >= C:
        start = mid + 1
        result = mid
    # 공유기 설치 수가 목표 보다 작으면 공유기 사이 거리 줄임
    else:
        end = mid - 1

print(result)