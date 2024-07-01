# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList):
        self.lst = nestedList
        self.iter = None
        self.currIdx = 0

    def next(self) -> int:

        # self.iter 가 None 이 아닐 때 = 현재 탐색 중인 요소가 list 일 때
        if self.iter:
            try:
                return self.iter.__next__()
            except StopIteration:
                self.iter = None
                self.currIdx += 1
                return self.next()

        else:
            currE = self.lst[self.currIdx]

            # 다음 요소가 정수일 때
            if type(currE) is int:
                self.iter = None
                self.currIdx += 1

                return currE

            # 다음 요소가 list 일 때
            elif type(currE) is list:
                self.iter = currE.__iter__()

                return self.iter.__next__()


    def hasNext(self) -> bool:
        if self.iter:
            return self.iter.hasNext()


if __name__ == "__main__":
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator([[1,1],2,[1,1]]), []
    i, v = NestedIterator([1,[4,[6]]]), []
    # while i.hasNext():
    for _ in range(5):
        v.append(i.next())
    print(v)