import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает файл на чтение в указанной кодировке и возвращает его содержимое.
    Если файл не найден или кодировка не подходит, ошибки пробрасываются наружу.
    """
    p = Path(path)
    # FileNotFoundError и UnicodeDecodeError пусть «всплывают» — это нормально
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Создает/перезаписывает CSV с разделителем ','.
    Опционально записывает header первой строкой.
    Проверяет, что все строки имеют одинаковую длину.
    """
    p = Path(path)
    rows = list(rows)

    # Проверка, что каждая строка имеет одинаковую длину (Требование Задания А)
    if rows:
        expected_len = len(rows[0])
        for r in rows:
            if len(r) != expected_len:
                raise ValueError(f"Все строки должны иметь одинаковую длину. Ожидалось {expected_len}, получено {len(r)}")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


# ★ (опционально, но полезно)
def ensure_parent_dir(path: str | Path) -> None:
    """Создает родительские директории, если их нет."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)