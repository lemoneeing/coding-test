import sys
input = sys.stdin.readline

def dijkstra(x1, y1, x2, y2, graph):
    # graph[x1][y1] 은 start 에서 해당 지점까지의 최소 거리
    #
    pass

def solution():
    # 모든 정점에서 2 까지의 거리 계산(2는 단 하나)
    # = 2 에서 다른 모든 정점으로까지의 거리 계산 = 다익스트라
    # 모든 정점 사이의 거리가 1로 동일하므로 2를 중심으로 가장 가까운 곳부터 탐색해야 함. = BFS
    n, m = map(int, input().split())
    board = []
    start = None # 2의 위치
    for r in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        if 2 in row:
            start = (r, row.index(2))

