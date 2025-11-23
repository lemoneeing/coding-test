import sys
input = sys.stdin.readline


def solution():
    testcase = int(input().strip())
    for _ in range(testcase):
        n = int(input().strip())
        pn_list = [input().strip() for _ in range(n)]

        pn_list.sort()
        is_consistent = True
        for i, curr in enumerate(pn_list):
            if i == n-1:
                break

            if pn_list[i+1].startswith(curr):
                is_consistent = False
                break

        if is_consistent:
            print('YES')
        else:
            print('NO')
solution()
