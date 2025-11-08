import sys
import operator
from itertools import permutations, product

input = sys.stdin.readline

'''
순열 추출
연산자 조합 추출
괄호 연산
'''

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def calculate(num1, opt, num2):
    if opt == '+':
        return num1 + num2
    elif opt == '-':
        return num1 - num2
    elif opt == '*':
        return num1 * num2
    else:
        if num2 == 0 or (num1 % num2 != 0):
            raise ValueError
        return num1 // num2


def combine_expressions(nums, opts, fmt):
    result = None
    try:
        if fmt == 0:  # 1+2+3+4 형태
            result = calculate(calculate(calculate(nums[0], opts[0], nums[1]), opts[1], nums[2]), opts[2], nums[3])
        elif fmt == 1:  # (1+(2+3))+4 형태
            result = calculate(calculate(nums[0], opts[0], calculate(nums[1], opts[1], nums[2])), opts[2], nums[3])
        elif fmt == 2:  # 1+((2+3)+4) 형태
            result = calculate(nums[0], opts[0], calculate(calculate(nums[1], opts[1], nums[2]), opts[2], nums[3]))
        elif fmt == 3:  # 1+(2+(3+4)) 형태
            result = calculate(nums[0], opts[0], calculate(nums[1], opts[1], calculate(nums[2], opts[2], nums[3])))
        else: # (1+2)+(3+4)) 형태
            result = calculate(calculate(nums[0], opts[0], nums[1]), opts[1], calculate(nums[2], opts[2], nums[3]))

        # 정수 결과만 유효
        if result == int(result):
            return int(result)

    except ValueError:
        return None


def solution():
    case_idx = 1
    while True:
        results = set()
        nums = list(map(int, input().split()))
        if sum(nums) == 0:
            break

        for perms in permutations(nums):
            for opts in product(['+', '-', '*', '/'], repeat=3):
                for i in range(5):
                    res = combine_expressions(perms, opts, i)

                    if res is not None:
                        results.add(res)

        sorted_res = sorted(results)
        max_start = curr_start = prev = sorted_res[0]
        max_len = curr_len = 1
        for j, curr in enumerate(sorted_res):
            if j > 0:
                if curr == prev + 1:
                    curr_len += 1
                else:
                    if curr_len >= max_len:
                        max_start = curr_start
                        max_len = curr_len
                    curr_start = curr
                    curr_len = 1

            prev = curr

        if curr_len >= max_len:
            max_start = curr_start
            max_len = curr_len

        print(f"Case {case_idx}: {max_start} to {max_start + max_len - 1}")
        case_idx += 1


solution()
