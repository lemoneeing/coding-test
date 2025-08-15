import sys

input = sys.stdin.readline

def solution():
    H, W = map(int, input().split())
    highest = 0
    blocks = list(map(int, input().split()))

    ans = 0             # 우물: 빗물이 고이는 공간
    start = [blocks[0]] # 우물의 앞 부분이 될 블록
    end = []            # 우물의 나머지 부분이 될 블록

    for b in blocks[1:]:

        # 현재 블록이 start 블록보다 낮으면, end stack 에 현재 블록 삽입
        if b < start[0]:
            end.append(b)

        # 현재 블록이 시작 블록보다 크거나 같으면,
        else:
            high = min(b, start.pop())      # start 블록과 현재 블록 중 더 낮은 블록으로 우물 높이 결정
            while end:
                ans += (high - end.pop())   # 우물 크기 계산
            start.append(b) # 새로운 시작 블록(현재 블록) 삽입

    # start 블록부터 마지막 블록까지의 우물 크기 계산
    if len(end) >= 2:
        curr = end.pop()
        while end:
            if end[-1] < curr:
                ans += min(curr, start[-1]) - end.pop()
            else:
                curr = end.pop()

    sys.stdout.write(f"{ans}")

solution()
