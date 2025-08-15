import sys

input = sys.stdin.readline

def solution():
    H, W = map(int, input().split())
    highest = 0
    blocks = list(map(int, input().split()))
    ans = 0

    start = [blocks[0]]
    end = []
    for b in blocks[1:]:
        # 현재 블록이 시작 블록보다 낮으면
        if b < start[0]:
            end.append(b) # end stack 에 현재 블록 삽입
        # 현재 블록이 시작 블록보다 크거나 같으면
        else:
            high = min(b, start[0]) # 더 낮은 블록으로 높이 고정
            while end:
                ans += (high - end.pop()) # 시작 블록까지의 공간 계산
            start.pop()
            start.append(b) # 새로운 시작 블록(현재 블록) 삽입

    if len(end) >= 2:
        curr = end.pop()
        while end:
            if end[-1] < curr:
                ans += min(curr, start[-1]) - end[-1]
            else:
                curr = end[-1]
            end.pop()

    sys.stdout.write(f"{ans}")

solution()
