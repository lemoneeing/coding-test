from copy import deepcopy


def solution(triangle):
    dp = [triangle[0]]

    for i in range(1, len(triangle)):
        if len(dp) < i+1:
            dp.append([])

        for j in range(0, len(triangle[i])):
            # dp[1][0] = dp[0][0] + t[1][0] | dp[1][1] = dp[0][0] + t[1][1]
            # dp[2][0] = dp[1][0] + t[2][0] | dp[2][1] = max(dp[1][0] + t[2][1], dp[1][1] + t[2][1]) | dp[2][2] = dp[1][2] + t[2][2]
            # dp[3][0] = dp[2][0] + t[3][0] | dp[3][1] = max(dp[2][0] + t[3][1], dp[2][1] + t[3][1]) | dp[3][2] = max(dp[2][1] + t[3][2], dp[2][2] + t[3][2]) | dp[3][3] = dp[2][2] + t[3][3]


            if j == 0:
                # dp[i][j] = dp[i-1][j] + triangle[i][j]
                dp[i].append(dp[i-1][j] + triangle[i][j])

            elif j == len(triangle[i]) - 1:
                # dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                dp[i].append(dp[i-1][j-1] + triangle[i][j])

            else:
                # dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])

    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))