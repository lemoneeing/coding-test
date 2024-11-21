from typing import List

# 예전에 푼 적 있음.
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         ans = 0
#         n, m = len(matrix), len(matrix[0])
#         for i in range(0, n):
#             for j in range(0, m):
#
#                 if i == 0 or j == 0:
#                     ans += matrix[i][j]
#
#                 elif matrix[i][j] and matrix[i - 1][j] and matrix[i][j - 1]:
#                     if matrix[i - 1][j] == matrix[i][j - 1]:
#                         size = matrix[i - 1][j]
#                         if matrix[i - size][j - size]:
#                             size += 1
#                         ans += size
#                     else:
#                         # matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + 1
#                         ans += min(matrix[i - 1][j], matrix[i][j - 1]) + 1
#
#         return ans


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
