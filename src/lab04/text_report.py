import sys
from pathlib import Path
from collections import Counter
import argparse

# 1. Настраиваем пути для импорта из src/lib и src/lab04
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parent.parent.parent  # папка python_labs
SRC_DIR = PROJECT_ROOT / "src"
LAB04_DIR = SRC_DIR / "lab04"

# Добавляем пути в sys.path, чтобы импорты работали при любом запуске
sys.path.append(str(SRC_DIR))
sys.path.append(str(LAB04_DIR))

# 2. Импорты с обработкой ошибок
try:
    from lib.text import normalize, tokenize, top_n
    from io_txt_csv import read_text, write_csv, ensure_parent_dir
except ImportError as e:
    print(f"ОШИБКА ИМПОРТА: {e}")
    print("Убедитесь, что в файле src/lib/text.py есть функции normalize, tokenize, top_n")
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
    sorted_items = sorted_word_counts(freq)

    ensure_parent_dir(out_path)
    write_csv(sorted_items, out_path, header=("word", "count"))

    # ТОЧНО ТАКОЙ ЖЕ ВЫВОД, КАК НА СКРИНШОТЕ
    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    print("слово   | частота")
    print("-------------------")
    
    # Форматируем строки: выравниваем по левому краю
    for word, count in top_n(freq, 5):
        print(f"{word:<7} | {count}")

def process_multiple_files(in_paths: list[Path], per_file_path: Path, total_path: Path, encoding: str = "utf-8") -> None:
    per_file_rows = []
    total_freq = Counter()

    for path in in_paths:
        if not path.exists():
            print(f" Файл {path} не найден, пропускаем.")
            continue
        text = read_text(path, encoding=encoding)
        freq = frequencies_from_text(text)
        total_freq.update(freq)
        for word, count in sorted_word_counts(freq):
            per_file_rows.append((path.name, word, count))

    per_file_rows.sort(key=lambda x: (x[0], -x[2], x[1]))
    ensure_parent_dir(per_file_path)
    write_csv(per_file_rows, per_file_path, header=("file", "word", "count"))

    total_rows = sorted_word_counts(dict(total_freq))
    ensure_parent_dir(total_path)
    write_csv(total_rows, total_path, header=("word", "count"))

def main() -> None:
    parser = argparse.ArgumentParser(description="Генерация отчётов по текстовой статистике.")
    
    # По умолчанию берем файлы из папки data/lab04, так как они там есть
    parser.add_argument("--in", dest="inputs", nargs="+", type=Path,
                        default=[PROJECT_ROOT / "data" / "lab04" / "input.txt"])
    parser.add_argument("--out", dest="output", type=Path, 
                        default=PROJECT_ROOT / "data" / "lab04" / "report.csv")
    parser.add_argument("--encoding", default="utf-8")
    parser.add_argument("--per-file", dest="per_file", type=Path)
    parser.add_argument("--total", dest="total", type=Path)

    args = parser.parse_args()

    # Если передано больше одного файла - включаем режим нескольких файлов (★)
    if len(args.inputs) > 1:
        # Если пользователь не указал пути для сохранения, ставим дефолтные
        if not args.per_file:
            args.per_file = PROJECT_ROOT / "data" / "lab04" / "report_per_file.csv"
        if not args.total:
            args.total = PROJECT_ROOT / "data" / "lab04" / "report_total.csv"
            
        process_multiple_files(args.inputs, args.per_file, args.total, args.encoding)
    else:
        # Базовый режим (один файл)
        process_single_file(args.inputs[0], args.output, args.encoding)

if __name__ == "__main__":
    main()