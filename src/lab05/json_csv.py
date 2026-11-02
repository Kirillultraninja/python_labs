"""Модуль для конвертации между JSON и CSV.

Реализует функции:
- json_to_csv: JSON (список словарей) → CSV.
- csv_to_json: CSV → JSON (список словарей).

Все функции работают только с файлами (без вывода в stdout),
используют кодировку UTF-8 и стандартные библиотеки json, csv, pathlib.
"""

import csv
import json
from pathlib import Path
from typing import Any


def _ensure_parent_dir(path: Path) -> None:
    """Создаёт родительский каталог для файла, если его нет."""
    path.parent.mkdir(parents=True, exist_ok=True)


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.

    Поддерживает список словарей [{...}, {...}]. Отсутствующие поля
    заполняются пустыми строками. Порядок колонок — как в первом объекте.

    Args:
        json_path: Путь к исходному JSON-файлу.
        csv_path: Путь к создаваемому CSV-файлу.

    Raises:
        FileNotFoundError: Если исходный файл не существует.
        ValueError: Если JSON пуст, содержит не список или элементы не словари.
    """
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    if json_file.suffix.lower() != ".json":
        raise ValueError(f"Ожидался файл .json, получен: {json_file.suffix}")

    with json_file.open(encoding="utf-8") as f:
        try:
            data: Any = json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError("Некорректный JSON или пустой файл") from exc

    # Валидация структуры
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # Формируем порядок колонок по первому объекту
    fieldnames = list(data[0].keys())

    csv_file = Path(csv_path)
    _ensure_parent_dir(csv_file)

    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            # Заполняем отсутствующие ключи пустыми строками
            full_row = {key: row.get(key, "") for key in fieldnames}
            writer.writerow(full_row)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей).

    Первая строка CSV считается заголовком. Значения сохраняются как строки.
    Результат записывается с параметрами ensure_ascii=False и indent=2.

    Args:
        csv_path: Путь к исходному CSV-файлу.
        json_path: Путь к создаваемому JSON-файлу.

    Raises:
        FileNotFoundError: Если исходный файл не существует.
        ValueError: Если CSV пуст или не содержит заголовка.
    """
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался файл .csv, получен: {csv_file.suffix}")

    with csv_file.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV-файл пуст или не содержит заголовка")
        rows = list(reader)
        if not rows:
            raise ValueError("CSV-файл не содержит данных")

    json_file = Path(json_path)
    _ensure_parent_dir(json_file)

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # Демонстрационный запуск: python -m src.lab05.json_csv
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("JSON ↔ CSV конвертации выполнены.")