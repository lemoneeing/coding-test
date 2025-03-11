import sys
input = sys.stdin.readline

def solution():
    n, W, L = map(int, input().split())
    trucks = list(map(int, input().split()))
    brg = []
    w_on_brg = 0
    cost = 0
    while trucks:
        nxt_tr = trucks[0]
        if w_on_brg + nxt_tr <= L:
            brg.append(trucks.pop(0))
            cost += 1
        else:
            cost += (W - len(brg))
            brg.pop(0)

        if len(brg) == W:
            brg.pop(0)

        if not trucks and brg: # 다리에 올라 가지 못한 트럭이 없음.
            cost += W

    sys.stdout.write(f"{cost}")

solution()

# # GPT 풀이
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# def solution():
#     n, W, L = map(int, input().split())
#     trucks = list(map(int, input().split()))
#
#     bridge = deque([0] * W)  # 다리 길이를 고려한 큐
#     total_weight = 0  # 현재 다리 위에 있는 트럭들의 총 무게
#     time = 0  # 경과 시간
#
#     while trucks or total_weight > 0:
#         time += 1
#
#         # 다리 맨 앞의 트럭을 내림
#         total_weight -= bridge.popleft()
#
#         if trucks:
#             # 다음 트럭을 다리에 올릴 수 있는지 확인
#             if total_weight + trucks[0] <= L:
#                 truck = trucks.pop(0)
#                 bridge.append(truck)
#                 total_weight += truck
#             else:
#                 bridge.append(0)  # 트럭을 올릴 수 없으면 빈 공간 유지
#
#     print(time)
# solution()