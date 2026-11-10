"""CLI-конвертеры данных: json2csv, csv2json, csv2xlsx."""

import argparse
import sys

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def cmd_json2csv(args: argparse.Namespace) -> None:
    json_to_csv(args.input, args.output)


def cmd_csv2json(args: argparse.Namespace) -> None:
    csv_to_json(args.input, args.output)


def cmd_csv2xlsx(args: argparse.Namespace) -> None:
    csv_to_xlsx(args.input, args.output)


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-конвертеры данных лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", required=True)

    commands = [
        ("json2csv", cmd_json2csv, "Конвертировать JSON в CSV"),
        ("csv2json", cmd_csv2json, "Конвертировать CSV в JSON"),
        ("csv2xlsx", cmd_csv2xlsx, "Конвертировать CSV в XLSX"),
    ]

    for name, func, help_text in commands:
        p = subparsers.add_parser(name, help=help_text)
        p.add_argument("--in", dest="input", required=True, help="Входной файл")
        p.add_argument("--out", dest="output", required=True, help="Выходной файл")
        p.set_defaults(func=func)

    args = parser.parse_args()

    try:
        args.func(args)
        print(f"Успешно: {args.input} → {args.output}")
    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка валидации: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()