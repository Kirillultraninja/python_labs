from pathlib import Path
import sys

# 1. Исправляем импорт, так как файлы лежат в одной папке (src/lab04)
from io_txt_csv import read_text, write_csv, ensure_parent_dir

# 2. Определяем корень проекта (python_labs), чтобы правильно находить папку data
# __file__ - это путь к tests.py (src/lab04/tests.py)
# .parent.parent.parent поднимает нас на 3 уровня вверх до папки python_labs
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "lab04"

def setup_test_data():
    """Создает папку data/lab04 и тестовые файлы в ней."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Вход для базовой версии
    (DATA_DIR / "input.txt").write_text("Привет, мир! Это базовый тест ЛР4.", encoding="utf-8")
    
    # 2. Входы для задания со звездочкой (несколько файлов)
    (DATA_DIR / "a.txt").write_text("Текст из файла А. Привет мир.", encoding="utf-8")
    (DATA_DIR / "b.txt").write_text("Текст из файла Б. Мир привет.", encoding="utf-8")
    
    print(f"✅ Тестовые файлы созданы в папке: {DATA_DIR}")

def run_tests():
    print("\n--- Запуск мини-тестов ---")
    
    # Пути к файлам
    input_txt = DATA_DIR / "input.txt"
    check_csv = DATA_DIR / "check.csv"
    
    # ==========================================
    # 1. Базовый тест из скриншота
    # ==========================================
    txt = read_text(input_txt)
    print(f"1. read_text('{input_txt.name}'):\n   Вернул: '{txt}'")
    
    # Создаст CSV
    write_csv([("word", "count"), ("test", 3)], check_csv)
    print(f"2. write_csv создал файл: {check_csv.name}")

    # ==========================================
    # 2. Проверка краевых случаев (Edge Cases)
    # ==========================================
    print("\n--- Проверка краевых случаев ---")

    # А) Пустой файл -> возвращается пустая строка
    empty_txt_path = DATA_DIR / "empty.txt"
    empty_txt_path.write_text("", encoding="utf-8")
    empty_txt = read_text(empty_txt_path)
    print(f"3. Чтение пустого файла: '{empty_txt}' (длина: {len(empty_txt)})")
    assert empty_txt == "", "Ошибка: пустой файл должен возвращать пустую строку"

    # Б) write_csv с пустым rows и header=None -> пустой файл (0 строк)
    empty_csv = DATA_DIR / "empty.csv"
    write_csv([], empty_csv, header=None)
    empty_csv_size = empty_csv.stat().st_size
    print(f"4. write_csv(пустой rows, header=None): размер файла = {empty_csv_size} байт")
    assert empty_csv_size == 0, "Ошибка: файл должен быть абсолютно пустым"

    # В) write_csv с пустым rows и header=("a", "b") -> только заголовок
    header_only_csv = DATA_DIR / "header_only.csv"
    write_csv([], header_only_csv, header=("a", "b"))
    header_content = header_only_csv.read_text(encoding="utf-8")
    print(f"5. write_csv(пустой rows, header=('a','b')): содержимое = '{header_content.strip()}'")
    assert header_content.strip() == "a,b", "Ошибка: файл должен содержать только заголовок"

    # Г) Проверка ValueError при разной длине строк (из Задания А)
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