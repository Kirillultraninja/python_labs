def linear_search(nums, x):
    """Индекс первого вхождения x или -1.
    Не требует сортировки.
    """
    for i, val in enumerate(nums):
        if val == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """Индекс любого вхождения x в ОТСОРТИРОВАННОМ списке или -1.
    На неотсортированном списке результат не определён.
    """
    lo, hi = 0, len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def two_sum_brute(nums, target):
    """Перебор пар (i, j), i < j, сумма nums[i] + nums[j] == target.
    Возвращает (i, j) или None.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target):
    """Один проход со словарём «значение → индекс».
    Возвращает (i, j) с i < j или None.
    При нескольких ответах допустим любой.
    """
    seen = {}
    for j, val in enumerate(nums):
        need = target - val
        if need in seen:
            i = seen[need]
            return (i, j) if i < j else (j, i)
        seen[val] = j
    return None
