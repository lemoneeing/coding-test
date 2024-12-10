class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        length_of_num = len(num)
        start = 0
        fe = 1
        while fe < length_of_num//2:
            be = fe + 1
            while be < length_of_num:
                curr_sum = str(int(num[start:fe]) + int(num[fe:be]))
                if num[be:] == curr_sum:
                    return True
                else:
                    if num[be:].startswith(curr_sum):
                        start = fe
                        fe = be
                        be += len(curr_sum)
                    else:
                        be += 1
            fe += 1

        return False

# print(Solution().isAdditiveNumber('231336497')) #True
# print(Solution().isAdditiveNumber('1752227381')) #False
# print(Solution().isAdditiveNumber('17522274976125')) #True
print(Solution().isAdditiveNumber('011112')) # False
# print(Solution().isAdditiveNumber('000')) # True
# print(Solution().isAdditiveNumber('12122436')) # True
# print(Solution().isAdditiveNumber('12012122436')) # True