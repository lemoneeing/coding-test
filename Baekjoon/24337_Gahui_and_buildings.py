import sys
input = sys.stdin.readline

def solution():
    N, a, b = map(int, input().strip().split())

    if a == N == b:
        sys.stdout.write('-1')

    ans = []

    curr = 1
    # curr < a 일 동안 ans 에 1 부터 오름차순 추가
    while curr < a:
        ans.append(curr)
        if N - len(ans) < b:
            sys.stdout.write('-1')
            return
        curr += 1

    # a loop 완료 & N - len(ans) >= b 이면 N-len(ans)-b 만큼 0 추가
    if N - len(ans) >= b:
        last = ans[-1]
        ans.extend([0]*(N-len(ans)-b))

    # ans 의 0 제외 마지막 숫자와 동일한 숫자부터 1씩 내림차순 추가
    curr = last
    while last-curr < b:
        ans.append(curr)
        curr -= 1

    sys.stdout.write(' '.join(list(map(str, ans))))

solution()