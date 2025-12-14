import math
import sys
input = sys.stdin.readline


def find(group, v):
    if group[v] != v:
        group[v] = find(group, group[v])  # 경로 압축
    return group[v]

def union(group, b, s):

    parent_of_b = find(group, b)
    parent_of_s = find(group, s)

    if parent_of_b == parent_of_s:
        return False

    root = parent_of_b if parent_of_b < parent_of_s else parent_of_s
    child = parent_of_b if parent_of_b > parent_of_s else parent_of_s

    group[child] = root

    return True

def solution():
    N, M = map(int, input().split())
    gods = [list(map(int, input().split())) for _ in range(N)]
    gods.insert(0, ())
    group = list(range(N + 1))
    min_dist = 0
    for _ in range(M):
        u, v = map(int, input().split())

        # 연결된 모든 정점들의 거리 초기화
        min_dist += math.sqrt((abs(gods[u][0] - gods[v][0]) ** 2) + (abs(gods[u][1] - gods[v][1]) ** 2))

        # 더 작은 값을 그룹 ID 로 설
        parent = u if u < v else v
        child = v if u < v else u

        parent_gid = find(group, parent)
        if parent_gid != parent:
            group[parent] = parent_gid
            group[child] = parent_gid
        else:
            group[child] = parent

        min_gid = min(min_gid, parent_gid)

    for i, g_r, g_c in enumerate(gods):
        if i == 0:
            continue


    ans = ''

solution()
