import sys
from tabnanny import check

input = sys.stdin.readline

# def partition(arr, indices, low, high):
#     """
#     퀵소트의 파티션 함수입니다.
#     값 배열(arr)을 기준으로 인덱스 배열(indices)을 정렬합니다.
#     피벗은 인덱스 배열의 high 위치에 해당하는 값 배열의 요소로 선택합니다.
#     """
#     pivot_value = arr[indices[high]]  # 피벗 값 (실제 값 배열의 요소)
#     i = low - 1  # 피벗보다 작은 요소들의 마지막 인덱스
#
#     for j in range(low, high):
#         # 현재 요소가 피벗보다 작거나 같으면
#         if arr[indices[j]] <= pivot_value:
#             i += 1
#             # 인덱스 배열에서 요소 교환
#             indices[i], indices[j] = indices[j], indices[i]
#
#     # 피벗을 올바른 위치로 이동시키기 위해 인덱스 교환
#     indices[i + 1], indices[high] = indices[high], indices[i + 1]
#     return i + 1  # 피벗의 최종 위치 인덱스
#
#
# def quick_sort_indices(arr, indices, low, high):
#     """
#     퀵소트 주 함수입니다.
#     값 배열(arr)을 기준으로 인덱스 배열(indices)을 재귀적으로 정렬합니다.
#     """
#     if low < high:
#         # 파티셔닝하여 피벗 위치를 찾음
#         pi = partition(arr, indices, low, high)
#
#         # 피벗을 기준으로 좌우 부분 배열에 대해 재귀적으로 퀵소트 수행
#         quick_sort_indices(arr, indices, low, pi - 1)
#         quick_sort_indices(arr, indices, pi + 1, high)
#
#
# def get_sorted_indices_by_quicksort(arr):
#     """
#     주어진 배열의 요소 크기에 따라 정렬된 인덱스 배열을 반환합니다.
#     퀵소트 방식을 사용합니다.
#     """
#     n = len(arr)
#     if n == 0:
#         return []
#
#     # 초기 인덱스 배열 생성 (0, 1, 2, ..., n-1)
#     indices = list(range(n))
#
#     # 퀵소트를 사용하여 인덱스 배열 정렬
#     quick_sort_indices(arr, indices, 0, n - 1)
#
#     return indices
#

# 예제 사용법
# if __name__ == "__main__":
#     unsorted_array = [50, 20, 80, 10, 70, 40, 30, 60, 90, 0]
#
#     print(f"원래 배열: {unsorted_array}")
#
#     sorted_indices = get_sorted_indices_by_quicksort(unsorted_array)
#     print(f"요소 크기 순으로 정렬된 인덱스 배열: {sorted_indices}")
#
#     # 정렬


def partition(arr, low, high):
    """
    퀵소트의 파티션 함수입니다.
    값 배열(arr)을 기준으로 인덱스 배열(indices)을 정렬합니다.
    피벗은 인덱스 배열의 high 위치에 해당하는 값 배열의 요소로 선택합니다.
    """
    pivot_value = arr[high]  # 피벗 값 (실제 값 배열의 요소)
    i = low - 1  # 피벗보다 작은 요소들의 마지막 인덱스

    for j in range(low, high):
        # 현재 요소가 피벗보다 작거나 같으면
        if arr[j] <= pivot_value:
            i += 1
            # 인덱스 배열에서 요소 교환
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗을 올바른 위치로 이동시키기 위해 인덱스 교환
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # 피벗의 최종 위치 인덱스


def quick_sort_indices(arr, low, high):
    """
    퀵소트 주 함수입니다.
    값 배열(arr)을 기준으로 인덱스 배열(indices)을 재귀적으로 정렬합니다.
    """
    if low < high:
        # 파티셔닝하여 피벗 위치를 찾음
        pi = partition(arr, low, high)

        # 피벗을 기준으로 좌우 부분 배열에 대해 재귀적으로 퀵소트 수행
        quick_sort_indices(arr, low, pi - 1)
        quick_sort_indices(arr, pi + 1, high)


def get_sorted_indices_by_quicksort(arr):
    """
    주어진 배열의 요소 크기에 따라 정렬된 인덱스 배열을 반환합니다.
    퀵소트 방식을 사용합니다.
    """
    n = len(arr)
    if n == 0:
        return []

    # 퀵소트를 사용하여 인덱스 배열 정렬
    quick_sort_indices(arr, 0, n - 1)

    return arr

# 퀵 정렬을 이용한 풀이
# def solution():
#     M, N = map(int, input().split())
#     universes = []
#     for _ in range(M):
#         universes.append(list(map(int, input().split())))
#
#     # 각 유니버스의 행성을 크기 기준 오름차순으로 정렬한 list 확보
#     sorted_universe = []
#     for un in universes:
#         sorted_universe.append(get_sorted_indices_by_quicksort(un))
#
#     # 각 유니버스의 각 행성 크기를 순위로 매긴 list 확보
#     star_ranks = []
#     for i, sorted_uv in enumerate(sorted_universe):
#         tmp = []
#         for uv in universes[i]:
#             tmp.append(sorted_uv.index(uv))
#         star_ranks.append([e for e in tmp])
#
#
#
#     # 순위가 같은 list 개수 count
#     ans = 0
#     checked = []
#     for rank in star_ranks:
#         if rank not in checked:
#             ans += star_ranks.count(rank) - 1
#             checked.append(rank)
#
#     sys.stdout.write(f"{ans}")


from bisect import bisect_left

def solution():
    M, N = map(int, input().split())
    universes = []
    for _ in range(M):
        universes.append(list(map(int, input().split())))

    sorted_uv = []
    uv_start_ranks = []
    for uv in universes:
        sorted_uv.append(sorted(uv))
        tmp = []
        for star in uv:
            tmp.append(bisect_left(sorted_uv[-1], star))
        uv_start_ranks.append([e for e in tmp])

    ans = 0
    checked = []
    for rank in uv_start_ranks:
        if rank not in checked:
            rank_cnt = uv_start_ranks.count(rank)
            if rank_cnt > 1:
                ans += int((rank_cnt ** 2 - rank_cnt) * 0.5)
            checked.append(rank)

    sys.stdout.write(f"{ans}")

solution()