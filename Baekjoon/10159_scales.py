import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    M = int(input())
    union = [i for i in range(N+1)]
    research = []
    for _ in range(M):
        comparison = list(map(int, input().split()))
        research.append(comparison)

    print(union)
    print(research)


solution()