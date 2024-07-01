from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def showRectangle(self):
        for i in range(len(self.rectangle)):
            print(self.rectangle[i])

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int)-> None:
        for sx in range(row1, row2+1):
            for sy in range(col1, col2+1):
                self.rectangle[sx][sy] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


if __name__ == "__main__":

    queries = ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
    params = [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]

    # queries = ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
    # params = [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]


    for i, query in enumerate(queries):
        if i == 0:
            obj = SubrectangleQueries(params[0][0])
            continue

        print(eval(f"obj.{query}({','.join(str(p) for p in params[i])})"))
        # obj.showRectangle()