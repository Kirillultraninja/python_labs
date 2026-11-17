import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    """Сравнивает fn(nums) с sorted(nums) на случайных списках.
    Проверяет, что исходный список не изменён.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), (f"{fn.__name__} ошиблась на {nums}: получено {result}, "f"ожидалось {sorted(nums)}")
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search():
    """Проверяет linear_search против list.index и binary_search
    на отсортированных данных.
    """
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-100, 100)

        # linear_search vs list.index
        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1
        got = linear_search(nums, x)
        assert got == expected, (
            f"linear_search({nums}, {x}) = {got}, ожидалось {expected}"
        )

        # binary_search на отсортированном списке
        sorted_nums = sorted(nums)
        got_bin = binary_search(sorted_nums, x)
        if got_bin != -1:
            assert sorted_nums[got_bin] == x, (f"binary_search вернул индекс {got_bin}, но значение не {x}")
        else:
            assert x not in sorted_nums, (f"binary_search не нашёл {x}, хотя он есть в {sorted_nums}")
def check_two_sum(trials=100):
    """Оба метода two_sum должны давать пару с нужной суммой или оба None."""
    for _ in range(trials):
        n = random.randint(2, 20)
        nums = [random.randint(-50, 50) for _ in range(n)]
        if n >= 2:
            i, j = random.sample(range(n), 2)
            target = nums[i] + nums[j]
        else:
            target = random.randint(-50, 50)

        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)

        # Проверяем корректность каждого результата
        if res_brute is not None:
            i, j = res_brute
            assert 0 <= i < j < len(nums) and nums[i] + nums[j] == target, (f"two_sum_brute вернул некорректную пару {res_brute} для {nums}, target={target}")
        if res_fast is not None:
            i, j = res_fast
            assert 0 <= i < j < len(nums) and nums[i] + nums[j] == target, (f"two_sum_fast вернул некорректную пару {res_fast} для {nums}, target={target}")

        # Оба должны найти пару или оба None
        assert (res_brute is None) == (res_fast is None), (f"Расхождение: brute={res_brute}, fast={res_fast} для {nums}, target={target}")
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK: все проверки пройдены")