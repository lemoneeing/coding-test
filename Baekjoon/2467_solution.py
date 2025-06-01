import sys
input = sys.stdin.readline

def find_nearest_index_to_zero(arr, s, e, last_vtz):
    mid = (s+e)//2
    vtz = abs(arr[mid])
    if last_vtz > vtz or vtz == 0:
        return mid

    if s < e:
        if arr[mid] < 0:
            return find_nearest_index_to_zero(arr, mid + 1, e, vtz)
        else:
            return find_nearest_index_to_zero(arr, s, mid - 1, vtz)

    return mid

def solution(N, solutions):
    N = int(N)
    solutions = list(map(int, solutions.split()))
    # N = int(input())
    # solutions = list(map(int, input().split()))

    start = find_nearest_index_to_zero(solutions, 0, N - 1, 0) # 0 과 가장 가까운 value 의 index 탐색 (이분탐색)
    if 0 < start < N-1:
        if abs(sum(solutions[start-1:start+1])) < abs(sum(solutions[start:start+2])):
            end = start-1
        else:
            end = start+1

        min_value_to_zero = 1000000001
        solution_pair = []
        while 0 <= start < N and 0 <= end < N:
            gap = solutions[start] + solutions[end]
            if abs(gap) < min_value_to_zero:
                min_value_to_zero = abs(gap)
                solution_pair = [solutions[start], solutions[end]]

            if gap < 0:
                end += 1
            else:
                start -= 1
    else:
        if start == 0:
            end = start + 1
        else:
            end = start -1
        solution_pair = [solutions[start], solutions[end]]

    solution_pair.sort()
    sys.stdout.write(f"{solution_pair[0]} {solution_pair[1]}\n")

solution("13", "-33 -8 -2 1 10 12 21 23 35 40 43 48 51")
solution("13", "-33 -29 -27 -25 -10 -8 -6 -3 -1 5 11 14 20")
solution("5", "-25 -21 -10 -6 -2")
solution("7", "-5 -3 1 2 5 6 8")
solution("5", "-1000 -500 -100 999 1002")
solution("4", "-4 -3 0 1")
solution("5", "-100 4 5 6 7")
solution("4", "-140 0 100 200")
solution("4", "-100 -2 -1 10")