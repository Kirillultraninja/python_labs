import sys
import os

# 1. Сначала добавляем путь к папке src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2. И только ПОСЛЕ этого делаем импорт
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    # 3. Сначала читаем текст из stdin
    text = sys.stdin.read()
    
    # 4. Потом проверяем его на пустоту
    if not text.strip():
        raise ValueError("Пустая строка")
        
    text1 = normalize(text)
    tokens = tokenize(text1)
    freq = count_freq(tokens)
    top = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for a, b in top:
        print(f"{a}:{b}")

if __name__ == "__main__":
    main()