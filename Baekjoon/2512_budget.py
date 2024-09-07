import sys
from queue import PriorityQueue

def solution():

    N = int(sys.stdin.readline())
    plans = list(map(int, sys.stdin.readline().split()))
    budget = int(sys.stdin.readline())

    def binary_search(s, e, limit):
        nonlocal plans

        if s >= e:
            return binary_search(0, len(plans)-1, limit - 1)

        share = 0
        avg = (plans[s] + plans[e]) // 2
        for n in plans:
            if n > avg:
                share += avg
            else:
                share += n

        if limit == share:
            return avg

        mid = s + e // 2
        # 배정 예산이 작은 경우
        if limit < share:
            return binary_search(s, mid, limit)
        # 배정 예산이 큰 경우
        else:
            return binary_search(mid + 1, e, limit)

    # 예산 요청 합이 예산 보다 작으면 제일 최댓값 출력
    if sum(plans) < budget:
        sys.stdout.write(f"{max(plans)}")

    # 예산 요청 합이 예산 보다 클 경우
    else:
        pq = PriorityQueue()
        for p in plans:
            pq.put(p)
        plans = list(pq.queue)
        binary_search(0, N-1, budget)

solution()