import sys
import heapq

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)] # 인접리스트
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))
        edges[v].append((u, w))

    cost = [sys.maxsize] * (N + 1)
    cost[1] = 0
    pq = [(0, 1)] # (비용, 목적지)
    while pq:
        curr_cost, m = heapq.heappop(pq)    # curr_cost: 출발지(1)에서 중간지점(m)까지 다이렉트로 이동하는 비용
                                            # m: 출발지(1)에서 가장 최소비용으로 갈 수 있는 노드.
        if cost[m] < curr_cost:             # 아래 for문에서 pq에 미리 추가되었던 노드의 비용이 그 사이 다른 중간지점(m)을 거쳐 더 작은 비용으로 갱신되었을 경우
            continue
        for d, w in edges[m]:               # 출발지(1) ~ 중간지점(m) ~ 목적지(d)까지 갈 수 있는 경로(간선) 중 최소 비용 탐색
            if cost[d] > curr_cost + w:     # cost[d]는 출발지(1) ~ 목적지(d)까지 다이렉트로 이동하는 비용
                cost[d] = curr_cost + w
                heapq.heappush(pq, (cost[d], d))  # 출발지에서 노드 m 을 거쳐 갈 수 있는 노드들을 힙으로 삽입. -> 그 중 가장 최소 비용인 노드부터 탐색하게 됨.(힙이니까)

    sys.stdout.write(f"{cost[N]}")

solution()