import csv
import os
import random
import sys
import timeit

# Импорт из 4-й лабораторной
from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast

SORT_FNS = {
    "bubble_sort": bubble_sort,
    "insertion_sort": insertion_sort,
    "selection_sort": selection_sort,
}


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def ensure_sample_data():
    os.makedirs("data/samples/lab07", exist_ok=True)
    for n in (1_000, 10_000, 100_000):
        path = f"data/samples/lab07/numbers_{n}.csv"
        if not os.path.exists(path):
            random.seed(42)
            nums = [random.randint(-1000, 1000) for _ in range(n)]
            with open(path, "w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(["value"])
                for v in nums:
                    w.writerow([v])
            log(f"[sample] создан {path}")


def read_numbers(path):
    with open(path, encoding="utf-8") as f:
        return [int(r["value"]) for r in csv.DictReader(f)]


def bench_sorts(n):
    rows = []
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")

    log(f"[sort n={n}] sorted ...")
    try:
        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("sort", n, "sorted", f"{t:.6f}"))
    except Exception as e:
        log(f"  sorted FAILED: {e}")
        rows.append(("sort", n, "sorted", "error"))

    for name, fn in SORT_FNS.items():
        if n >= 100_000:
            log(f"[sort n={n}] {name}: skipped (>=60s by complexity)")
            rows.append(("sort", n, name, ">60"))
            continue
        log(f"[sort n={n}] {name} ...")
        try:
            t = timeit.timeit(lambda: fn(data), number=1)
            rows.append(("sort", n, name, f"{t:.6f}"))
        except Exception as e:
            log(f"  {name} FAILED: {e}")
            rows.append(("sort", n, name, "error"))
    return rows


def bench_search():
    rows = []
    n = 100_000
    data = read_numbers(f"data/samples/lab07/numbers_{n}.csv")
    sorted_data = sorted(data)

    random.seed(42)
    n_queries = 1000
    queries = [random.choice(data) for _ in range(n_queries)]

    log(f"[search] linear_search ({n_queries} запросов) ...")
    try:
        t = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
        rows.append(("search", n, f"linear_search_x{n_queries}", f"{t:.6f}"))
    except Exception as e:
        log(f"  linear_search FAILED: {e}")
        rows.append(("search", n, "linear_search", "error"))

    log("[search] sort_for_binary ...")
    try:
        t = timeit.timeit(lambda: sorted(data), number=1)
        rows.append(("search", n, "sort_for_binary", f"{t:.6f}"))
    except Exception as e:
        log(f"  sort FAILED: {e}")
        rows.append(("search", n, "sort_for_binary", "error"))

    log(f"[search] binary_search ({n_queries} запросов) ...")
    try:
        t = timeit.timeit(lambda: [binary_search(sorted_data, q) for q in queries], number=1)
        rows.append(("search", n, f"binary_search_x{n_queries}", f"{t:.6f}"))
    except Exception as e:
        log(f"  binary_search FAILED: {e}")
        rows.append(("search", n, "binary_search", "error"))
    return rows


def bench_two_sum():
    rows = []
    for n in (1_000, 10_000):
        random.seed(42)
        nums = [random.randint(-1000, 1000) for _ in range(n)]
        i, j = random.sample(range(n), 2)
        target = nums[i] + nums[j]

        log(f"[two_sum n={n}] brute ...")
        try:
            t = timeit.timeit(lambda: two_sum_brute(nums, target), number=1)
            rows.append(("two_sum", n, "brute", f"{t:.6f}"))
        except Exception as e:
            log(f"  brute FAILED: {e}")
            rows.append(("two_sum", n, "brute", "error"))

        log(f"[two_sum n={n}] fast ...")
        try:
            t = timeit.timeit(lambda: two_sum_fast(nums, target), number=1)
            rows.append(("two_sum", n, "fast", f"{t:.6f}"))
        except Exception as e:
            log(f"  fast FAILED: {e}")
            rows.append(("two_sum", n, "fast", "error"))
    return rows


def save_csv(rows):
    os.makedirs("data/lab07", exist_ok=True)
    
    # Преобразуем в список кортежей для вашей функции
    csv_rows = [(t, n, impl, sec) for t, n, impl, sec in rows]
    
    # Вызываем вашу функцию из 4-й лабораторной
    write_csv(csv_rows, "data/lab07/bench.csv", header=["task", "n", "impl", "seconds"])
    
    log(f"[saved] data/lab07/bench.csv ({len(rows)} строк)")


def main():
    ensure_sample_data()
    random.seed(42)
    all_rows = []

    try:
        for n in (1_000, 10_000, 100_000):
            all_rows.extend(bench_sorts(n))
        all_rows.extend(bench_search())
        all_rows.extend(bench_two_sum())
    except Exception as e:
        log(f"FATAL: {e}")
    finally:
        save_csv(all_rows)

        print()
        print(f"{'task':<10} {'n':>8} {'impl':<26} {'seconds':>12}")
        print("-" * 60)
        for task, n, impl, sec in all_rows:
            print(f"{task:<10} {n:>8} {impl:<26} {sec:>12}")


if __name__ == "__main__":
    main()