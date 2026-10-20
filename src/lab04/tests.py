import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from io_txt_csv import read_text, write_csv, ensure_parent_dir

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "lab04"

def setup_test_data():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "input.txt").write_text("Привет, мир! Это базовый тест ЛР4.", encoding="utf-8")
    (DATA_DIR / "a.txt").write_text("Текст из файла А. Привет мир.", encoding="utf-8")
    (DATA_DIR / "b.txt").write_text("Текст из файла Б. Мир привет.", encoding="utf-8")

def run_tests():
    print("\n--- Запуск мини-тестов ---")
    input_txt = DATA_DIR / "input.txt"
    check_csv = DATA_DIR / "check.csv"

    txt = read_text(input_txt)
    print(f"1. read_text('{input_txt.name}'):\n   Вернул: '{txt}'")

    write_csv([("word", "count"), ("test", 3)], check_csv)
    print(f"2. write_csv создал файл: {check_csv.name}")

    print("\n--- Проверка краевых случаев ---")

    empty_txt_path = DATA_DIR / "empty.txt"
    empty_txt_path.write_text("", encoding="utf-8")
    empty_txt = read_text(empty_txt_path)
    print(f"3. Чтение пустого файла: '{empty_txt}' (длина: {len(empty_txt)})")
    assert empty_txt == "", "Ошибка: пустой файл должен возвращать пустую строку"

    empty_csv = DATA_DIR / "empty.csv"
    write_csv([], empty_csv, header=None)
    empty_csv_size = empty_csv.stat().st_size
    print(f"4. write_csv(пустой rows, header=None): размер файла = {empty_csv_size} байт")
    assert empty_csv_size == 0, "Ошибка: файл должен быть абсолютно пустым"

    header_only_csv = DATA_DIR / "header_only.csv"
    write_csv([], header_only_csv, header=("a", "b"))
    header_content = header_only_csv.read_text(encoding="utf-8")
    print(f"5. write_csv(пустой rows, header=('a','b')): содержимое = '{header_content.strip()}'")
    assert header_content.strip() == "a,b", "Ошибка: файл должен содержать только заголовок"

    error_csv = DATA_DIR / "error.csv"
    try:
        write_csv([("a", "b"), ("c",)], error_csv)
        print("6. Ошибка: ValueError не был вызван!")
    except ValueError as e:
        print(f"6. Успешно перехвачен ValueError: {e}")

    print("\n--- Все тесты пройдены успешно! ---")

if __name__ == "__main__":
    setup_test_data()
    run_tests()