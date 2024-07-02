def solution(numbers, target):
    answer = 0
    def dfs(plus, idx, sum):
        nonlocal answer

        if plus:
            sum += numbers[idx]
        else:
            sum -= numbers[idx]

        if idx == len(numbers) - 1:
            if sum == target:
                answer += 1
            return

        dfs(True, idx+1, sum)
        dfs(False, idx+1, sum)

    dfs(True, 0, 0)
    dfs(False, 0, 0)

    return answer

print(solution([4, 1, 2, 1], 4))