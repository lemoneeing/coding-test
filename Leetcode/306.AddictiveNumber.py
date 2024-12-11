class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for fi in range(1, len(num)):
            for si in range(fi+1, len(num)):
                first = num[:fi]
                second = num[fi:si]
                last = num[si:]
                if len(first) > 1 and first[0] == '0':
                    return False

                if len(second) > 1 and second[0] == '0':
                    break

                if len(last) > 1 and last[0] == '0' and int(last) != 0:
                    continue

                # 지금까지의 substring 은 additive seq 가 될 수 없으므로 first를 바꿔야 .
                if max(len(first), len(second)) > len(last):
                    break

                currSum = int(first) + int(second)
                while last.startswith(str(currSum)):
                    if currSum == int(last):
                        return True

                    last = last[len(str(currSum)):]
                    first = second
                    second = str(currSum)
                    currSum = int(first) + int(second)

        return False





# print(Solution().isAdditiveNumber('112358')) #True
# print(Solution().isAdditiveNumber('199100199')) #True
# print(Solution().isAdditiveNumber('231336497')) #True
# print(Solution().isAdditiveNumber('1752227381')) #False
# print(Solution().isAdditiveNumber('17522274976125')) #True
# print(Solution().isAdditiveNumber('011112')) # False
# print(Solution().isAdditiveNumber('000')) # True
# print(Solution().isAdditiveNumber('12122436')) # True
# print(Solution().isAdditiveNumber('12012122436')) # True
# print(Solution().isAdditiveNumber('198019823962')) # True
# print(Solution().isAdditiveNumber('0000')) # True
print(Solution().isAdditiveNumber('112358')) # True