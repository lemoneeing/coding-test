import sys
input = sys.stdin.readline

def solution():
    N, a, b = map(int, input().strip().split())

    if a == N == b:
        sys.stdout.write('-1')


solution()