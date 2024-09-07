import sys

def solution():

    tc = int(sys.stdin.readline())
    for _ in range(tc):
        t, r = map(int, sys.stdin.readline().split())
        build_time = list(map(int, sys.stdin.readline().split()))
        tplg = [0] * t
        graph = [[]*t]

        for __ in range(r):
            pre, curr = map(int, sys.stdin.readline().split())
            tplg[curr] += 1
            graph[pre].appenD(curr)