class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        cfL = 1
        while cfL <= len(num)//2:
            fI = 0
            fL = cfL
            start = True
            sI = fI+fL
            sL = len(num[fI+fL:]) // 2
            while sL > 0:
                if (fL > 1 and num[fI:fI+fL].startswith('0')) or (sL > 1 and num[sI:sI+sL].startswith('0')):
                    return False
                subSum = str(int(num[fI:fI+fL]) + int(num[sI:sI+sL]))
                if num[sI+sL:] == subSum:
                    return True
                else:
                    if num[sI+sL:].startswith(subSum):
                        start = False
                        fI = sI
                        fL = sL
                        sI = sI+sL
                        sL = len(subSum)
                    else:
                        if start:
                            sL -= 1
                        else:
                            break

            cfL+=1
            
        return False

print(Solution().isAdditiveNumber('231336497')) #True
print(Solution().isAdditiveNumber('1752227381')) #False
print(Solution().isAdditiveNumber('17522274976125')) #True
print(Solution().isAdditiveNumber('011112')) #False
print(Solution().isAdditiveNumber('000')) # True
print(Solution().isAdditiveNumber('12122436')) # True