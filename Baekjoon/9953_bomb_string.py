import sys

input = sys.stdin.readline

def solution():
    string = input().strip()
    bomb = list(input().strip())

    stack = []
    cache = []
    for s in string:
        if s != bomb[-1]:
            stack.append(s)
        else:
            cache.append(s)

            while len(cache) < len(bomb):
                if stack:
                    cache.append(stack.pop())
                else:
                    break

            cache.reverse()
            if cache != bomb:
                stack.extend(cache)
            cache = []

    if stack:
        for letter in stack:
            sys.stdout.write(letter)
    else:
        print("FRULA")

solution()