def solution(arr):
    dp = [0 for _ in arr]

    def dynamic_programming(operFlag, idx):
        nonlocal dp, sum

        if operFlag:
            dp[idx] = dp[idx-1] + arr[idx]
        else:
            dp[idx] = dp[idx-1] + (arr[idx] * -1)

        if sum < dp[idx]:
            sum = dp[idx]

        if idx >= len(arr) - 1:
            return

        dynamic_programming(not operFlag, idx+1)

    answer = 0
    sum = 0
    for i in range(len(arr)):
        dp[i] = sum = arr[i] * -1
        dynamic_programming(True, i)
        answer = sum if sum > answer else answer

    for i in range(len(arr)):
        dp[i] = sum = arr[i]
        dynamic_programming(False, i)
        answer = sum if sum > answer else answer

    answer = answer if answer > arr[-1] else arr[-1]

    return sum


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
# print(solution([2,3,7,16,19,20]))