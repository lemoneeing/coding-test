import sys

def solution():
    N = int(sys.stdin.readline().strip())
    bulbs = list(map(int, list(sys.stdin.readline().strip())))
    quiz = list(map(int, list(sys.stdin.readline().strip())))

    print(N)
    print(bulbs)
    print(quiz)


solution()