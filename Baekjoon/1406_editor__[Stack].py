import sys

def solution():
    sentence = sys.stdin.readline().strip()
    left = list(sentence)
    right = []
    
    M = int(sys.stdin.readline().strip())
    for _ in range(M):
        query = sys.stdin.readline().strip().split()
        if query[0] == 'L':
            if left:
                right.append(left.pop())
        elif query[0] == 'D':
            if right:
                left.append(right.pop())
        elif query[0] == 'B':
            if left: 
                left.pop()
        elif query[0] == 'P':
            left.append(query[1])
    
    sys.stdout.write(f"{''.join(left)}{''.join(reversed(right))}")
    
solution()
