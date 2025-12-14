import sys

input = sys.stdin.readline

MAX_OBJECT = 3
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상우하좌
ans = 'NO'


def can_teachers_find_students(crd_map, teachers):
    '''
    주어진 T 위치에서 학생을 감시할 수 있는 지 확인
    '''
    cor_len = len(crd_map)

    for tr, tc in teachers:
        for dr, dc in dirs:
            nr = tr + dr
            nc = tc + dc

            while 0 <= nr < cor_len and 0 <= nc < cor_len:
                if crd_map[nr][nc] == 'S':
                    return True
                else:
                    if crd_map[nr][nc] == 'O':
                        break
                    else:
                        nr += dr
                        nc += dc

    return False


def install_objects(crd_map, teachers, obj_cnt):
    '''
    백트래킹으로 장애물을 MAX_OBJECT 만큼 설치
    '''
    global MAX_OBJECT, ans

    # 종료 조건
    if obj_cnt == MAX_OBJECT:
        if not can_teachers_find_students(crd_map, teachers):
            ans = 'YES'
        return

    cor_len = len(crd_map)
    
    # 복도의 모든 빈 공간에 한 번 씩 장애물을 배치
    for r in range(cor_len):
        for c in range(cor_len):
            if crd_map[r][c] == 'X':

                # 장애물 배치
                if 0 <= r < cor_len and 0 <= c < cor_len:
                    prev = crd_map[r][c]
                    crd_map[r][c] = 'O'

                    install_objects(crd_map, teachers, obj_cnt + 1)

                    crd_map[r][c] = prev


def solution():
    global MAX_OBJECT, ans

    N = int(input().strip())

    corridors = []
    teachers = []
    for r in range(N):
        crd = list(input().split())
        for c in range(N):
            if crd[c] == 'T':
                teachers.append((r, c))

        corridors.append(crd)

    install_objects(corridors, teachers, 0)
    print(ans)


solution()