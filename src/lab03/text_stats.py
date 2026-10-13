import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
text = sys.stdin.read()
if text.strip() == "":
    raise ValueError("Пустая строка")
text = normalize(text)
tokens = tokenize(text)
freq = count_freq(tokens)
top = top_n(freq, n=5)
     
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")
for a, b in top:
    print(f"{a}:{b}")