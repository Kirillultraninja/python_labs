import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


def _ensure_parent_dir(path: Path) -> None:
    """Создаёт родительский каталог для файла, если его нет."""
    path.parent.mkdir(parents=True, exist_ok=True)


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    if csv_file.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался файл .csv, получен: {csv_file.suffix}")

    with csv_file.open(encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        raise ValueError("CSV-файл пуст")
    if not rows[0]:
        raise ValueError("CSV-файл не содержит заголовка")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Автоширина колонок (минимум 8 символов)
    for col_idx, column in enumerate(ws.columns, start=1):
        max_length = 0
        for cell in column:
            if cell.value is not None:
                max_length = max(max_length, len(str(cell.value)))
        adjusted_width = max(max_length, 8)  # как в ТЗ: не менее 8
        ws.column_dimensions[get_column_letter(col_idx)].width = adjusted_width

    xlsx_file = Path(xlsx_path)
    _ensure_parent_dir(xlsx_file)
    wb.save(xlsx_file)


if __name__ == "__main__":
    # Демонстрационный запуск: python -m src.lab05.csv_xlsx
    csv_to_xlsx("data/samples/people.csv", "data/out/tabl.xlsx")
    print("CSV → XLSX конвертация выполнена.")