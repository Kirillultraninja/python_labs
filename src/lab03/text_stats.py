import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")

import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from src.lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    text = sys.stdin.read()

    if not text.strip():
        raise ValueError("Пустая строка")

    text1 = normalize(text)
    tokens = tokenize(text1)
    freq = count_freq(tokens)
    top = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()