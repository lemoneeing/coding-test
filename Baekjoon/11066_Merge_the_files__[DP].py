import sys
from queue import PriorityQueue

input = sys.stdin.readline


def solution():
    case = int(input())
    for _ in range(case):
        file_cnt = int(input())
        pq = PriorityQueue(maxsize=file_cnt)

        files = list(map(int, input().split()))
        for f in files:
            pq.put(f)

        cost = []
        pair = []
        while not pq.empty():
            if len(pair) < 2:
                pair.append(files.pop(0))
            else:
                new_f = sum(pair)
                cost.append(new_f)
                pair = []




        sys.stdout.write(f"{sum(cost)}\n")


solution()
