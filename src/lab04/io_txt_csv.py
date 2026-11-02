import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает файл на чтение в указанной кодировке и возвращает его содержимое как одну строку.

    Если файл не найден — возбуждается FileNotFoundError.
    Если файл не может быть декодирован — возбуждается UnicodeDecodeError.
    Пользователь может выбрать другую кодировку, передав аргумент encoding (например, encoding="cp1251").
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Создаёт или перезаписывает CSV-файл с разделителем ','.

    :param rows: Список строк (кортежей или списков) для записи.
    :param path: Путь к создаваемому файлу.
    :param header: Опциональный заголовок (кортеж строк), записываемый первой строкой.
    :raises ValueError: Если хотя бы одна строка из 'rows' имеет длину, отличную от остальных.
    """
    p = Path(path)
    rows_list = list(rows)

    if rows_list:
        expected_len = len(rows_list[0])
        for row in rows_list:
            if len(row) != expected_len:
                raise ValueError(
                    f"Все строки должны иметь одинаковую длину. "
                    f"Ожидалось {expected_len}, получено {len(row)} в строке {row}."
                )

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows_list:
            w.writerow(r)

def ensure_parent_dir(path: str | Path) -> None:
    """
    Создаёт родительские директории, если они не существуют.
    Удобно вызывать перед записью файла.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)