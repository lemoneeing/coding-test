class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if num.startswith('0'):
            return False

        fI = 0
        fL = 1
        while fL <= len(num)//2:
            sI = fI+fL
            sL = len(num[fI+fL:]) // 2
            while sL > 0:
                subSum = str(int(num[fI:fI+fL]) + int(num[sI:sI+sL]))
                if num[sI+sL:] == subSum:
                    return True
                else:
                    if num[sI+sL:].startswith(subSum):
                        fI = sI
                        fL = sL
                        sI = sI+sL
                        sL = len(subSum)
                    else:
                        sL -= 1

            fL+=1
            
        return False

# print(Solution().isAdditiveNumber('231336497'))
# print(Solution().isAdditiveNumber('1752227381'))
print(Solution().isAdditiveNumber('17522274976125'))