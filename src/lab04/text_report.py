import sys
from pathlib import Path
from collections import Counter
import argparse

# Настраиваем пути для импорта (работает и при python file.py, и при python -m module)
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parent.parent.parent  # папка python_labs
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.append(str(SRC_DIR))

try:
    from lib.text import normalize, tokenize, top_n
    from lab04.io_txt_csv import read_text, write_csv, ensure_parent_dir
except ImportError as e:
    print(f"ОШИБКА ИМПОРТА: {e}")
    print("Убедитесь, что скрипт запускается из корня проекта (python_labs)")
    sys.exit(1)


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def process_single_file(in_path: Path, out_path: Path, encoding: str = "utf-8") -> None:
    if not in_path.exists():
        print(f"Ошибка: Файл {in_path} не найден!")
        return
    try:
        text = read_text(in_path, encoding=encoding)
    except Exception as e:
        print(f"Ошибка при чтении: {e}")
        return

    freq = frequencies_from_text(text)
    ensure_parent_dir(out_path)
    write_csv(sorted_word_counts(freq), out_path, header=("word", "count"))

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    print("слово   | частота")
    print("-------------------")
    for word, count in top_n(freq, 5):
        print(f"{word:<7} | {count}")


def process_multiple_files(in_paths: list[Path], per_file_path: Path, total_path: Path, encoding: str = "utf-8") -> None:
    per_file_rows = []
    total_freq = Counter()

    for path in in_paths:
        if not path.exists():
            continue
        text = read_text(path, encoding=encoding)
        freq = frequencies_from_text(text)
        total_freq.update(freq)
        for word, count in sorted_word_counts(freq):
            per_file_rows.append((path.name, word, count))

    # Сохраняем отчеты
    per_file_rows.sort(key=lambda x: (x[0], -x[2], x[1]))
    ensure_parent_dir(per_file_path)
    write_csv(per_file_rows, per_file_path, header=("file", "word", "count"))

    ensure_parent_dir(total_path)
    write_csv(sorted_word_counts(dict(total_freq)), total_path, header=("word", "count"))

    # --- ВЫВОД В КОНСОЛЬ (как на скрине) ---
    print(f"Всего слов: {sum(total_freq.values())}")
    print(f"Уникальных слов: {len(total_freq)}")
    print("Топ-5:")
    print("слово   | частота")
    print("-------------------")
    for word, count in top_n(total_freq, 5):
        print(f"{word:<7} | {count}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="inputs", nargs="+", type=Path,
                        default=[PROJECT_ROOT / "data" / "lab04" / "input.txt"])
    parser.add_argument("--out", dest="output", type=Path,
                        default=PROJECT_ROOT / "data" / "lab04" / "report.csv")
    parser.add_argument("--encoding", default="utf-8")
    parser.add_argument("--per-file", dest="per_file", type=Path)
    parser.add_argument("--total", dest="total", type=Path)

    args = parser.parse_args()

    # Если передано несколько файлов — включаем мультирежим
    if len(args.inputs) > 1:
        per_file = args.per_file or (PROJECT_ROOT / "data" / "lab04" / "report_per_file.csv")
        total = args.total or (PROJECT_ROOT / "data" / "lab04" / "report_total.csv")
        process_multiple_files(args.inputs, per_file, total, args.encoding)
    else:
        process_single_file(args.inputs[0], args.output, args.encoding)


if __name__ == "__main__":
    main()