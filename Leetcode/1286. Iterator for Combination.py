from typing import List


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.cmbLen = combinationLength
        self.answers = []

        self.backtrack(0, [])

    def backtrack(self, currIdx, subChars:List[str]):
        if len(subChars) == self.cmbLen:
            self.answers.append(subChars)

        while currIdx < len(self.characters):
            subChars.append(self.characters[currIdx])
            currIdx += 1
            self.backtrack(currIdx, subChars)
            subChars = subChars[:-1]

        self.backtrack(currIdx+1, subChars)


    def next(self) -> str:
        if len(self.currCmb) == self.cmbLen:
            return self.currCmb


    def hasNext(self) -> bool:
        pass


if __name__ == "__main__":
    c = CombinationIterator("abc", 2)

    # questions = ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    #
    # for q in questions:
    #     if q == "CombinationIterator":
    #         print(None)
    #
    #     print(eval(f"c.{q}()"))
    print(c.answers)