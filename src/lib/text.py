import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    text = text.strip()
    if casefold:
        text = text.casefold()
    else:
        text= text.lower()
    if yo2e:
        text = text.replace("Ё", "E").replace("ё","е")
    text = " ".join(text.split())
    return text

def tokenize(text: str):
    return re.findall(r"\w+(?:-\w+)*", text)

def count_freq(tokens: list[str]):
    m = dict()
    for i in range(len(set(tokens))):
        m[sorted(list(set(tokens)))[i]] = tokens.count(sorted(list(set(tokens)))[i])
    return m

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


if __name__ == "__main__":
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]
    assert top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2) == [("aa", 2), ("bb", 2)]
    print("Все тесты text.py успешно пройдены!")