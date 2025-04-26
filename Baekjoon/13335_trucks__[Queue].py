import sys
input = sys.stdin.readline

def solution():
    n, W, L = map(int, input().split())
    trucks = list(map(int, input().split()))
    brg = []
    cost = 0
    while trucks or sum(brg) > 0:
        cost += 1

        # 다리가 트럭으로 꽉 찼으면 맨 앞 트럭 이동 = 다리 탈출
        if len(brg) == W:
            brg.pop(0)
        
        if trucks:
            nxt_tr = trucks[0] # 남은 트럭 중 가장 앞 순서

            if sum(brg) + nxt_tr <= L: # 하중 여유 있으면 다리 위로 트럭 올리기
                brg.append(trucks.pop(0))
                continue
        # 남은 트럭이 없거나 다리 하중 여유 없으면 다리 위 트럭들만 한 칸 씩 이동
        brg.append(0)
        

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