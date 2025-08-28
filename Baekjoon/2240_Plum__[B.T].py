import sys

input = sys.stdin.readline


def solution():
    T, W = map(int, input().split())
    move = [False] * (T+1)
    curr = 1
    # 자두가 떨어지는 나무의 번호가 바뀌는 시간은 True, 유지되는 시간은 False
    for i in range(T):
        if curr == int(input()):
            move[i+1] = False
        else:
            move[i+1] = True
            curr = curr % 2 + 1



solution()
