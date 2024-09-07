import sys
def solution():
    game = {'Y': 1, 'F': 2, 'O': 3}

    N, G = sys.stdin.readline().split()
    player = []
    for _ in range(int(N)):
        player.append(sys.stdin.readline().strip())

    player = set(player)

    sys.stdout.write(f"{len(player)//game[G]}")

solution()