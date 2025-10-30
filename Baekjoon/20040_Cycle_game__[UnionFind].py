import sys
input = sys.stdin.readline


def find(child, tree):
    if child == tree[child]:
        return child

    return find(tree[child], tree)

def union(start, end, tree):
    start_parent = find(start, tree)
    end_parent = find(end, tree)

    if start_parent < end_parent:
        tree[end_parent] = start_parent
    else:
        tree[start_parent] = end_parent


def solution():
    n, m = map(int, input().strip().split())
    tree = [i for i in range(n)]
    for cnt in range(m):
        u, v = map(int, input().strip().split())

        if find(u, tree) == find(v, tree):
            print(cnt+1)
            return

        union(u, v, tree)

    print(0)

solution()