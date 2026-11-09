"""CLI-утилиты для работы с текстом: stats и cat."""

import argparse
import sys
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def cmd_stats(args: argparse.Namespace) -> None:
    """Анализ частот слов в текстовом файле."""
    path = Path(args.input)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    text = path.read_text(encoding="utf-8")
    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    top = top_n(freq, args.top)

    for word, count in top:
        print(f"{word}:{count}")


def cmd_cat(args: argparse.Namespace) -> None:
    """Вывод содержимого файла построчно (с опциональной нумерацией)."""
    path = Path(args.input)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if args.n:
                print(f"{i:6d}\t{line}", end="")
            else:
                print(line, end="")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CLI-утилиты лабораторной №6 (текстовые команды)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- подкоманда stats ---
    stats_parser = subparsers.add_parser(
        "stats", help="Анализ частот слов в тексте"
    )
    stats_parser.add_argument(
        "--input", required=True, help="Путь к входному текстовому файлу"
    )
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество топ-слов (по умолчанию 5)"
    )
    stats_parser.set_defaults(func=cmd_stats)

    # --- подкоманда cat ---
    cat_parser = subparsers.add_parser(
        "cat", help="Вывод содержимого файла построчно"
    )
    cat_parser.add_argument(
        "--input", required=True, help="Путь к файлу"
    )
    cat_parser.add_argument(
        "-n", action="store_true", help="Нумеровать строки"
    )
    cat_parser.set_defaults(func=cmd_cat)

    args = parser.parse_args()

    try:
        args.func(args)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()