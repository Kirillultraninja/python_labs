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

def top_n(freq: dict[str, int], n: int = 5):
    g = dict(sorted(freq.items(), key =lambda x: -x[1]))
    b= sorted(g.items(),key =lambda x: x[0])
    return b[:n]

if __name__ == '__main__':
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"

    assert tokenize("привет, мир!") == ["привет", "мир"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]


    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]

    print('Все кейсы успешно пройдены!')
    if input('хотите увидеть тест кейсы? [Y/n]') in ('y', 'Y', ''):
        print('Тест кейсы:')

        print(fr'''
        normalize

        "ПрИвЕт\nМИр\t" -> "{normalize('ПрИвЕт\nМИр\t')}"
        "ёжик, Ёлка" -> "{normalize('ёжик, Ёлка')}"
        "Hello\r\nWorld" -> "{normalize('Hello\r\nWorld')}"
        "  двойные   пробелы  " -> "{normalize('  двойные   пробелы  ')}"
        ''')

        print(fr'''
        tokenize

        "привет мир" -> "{tokenize('привет мир')}"
        "hello,world!!!" -> "{tokenize('hello,world!!!')}"
        "по-настоящему круто" -> "{tokenize('по-настоящему круто')}"
        "2025 год" -> "{tokenize('2025 год')}"
        "emoji 😀 не слово" -> "{tokenize('emoji 😀 не слово')}"
        ''')

        print(fr'''
        count_freq + top_n

        токены ["a","b","a","c","b","a"] -> частоты "{count_freq(['a', 'b', 'a', 'c', 'b', 'a'])}";
        top_n(..., n=2) -> "{top_n(count_freq(['a', 'b', 'a', 'c', 'b', 'a']), 2)}"

        токены ["bb","aa","bb","aa","cc"] -> "{count_freq(['bb', 'aa', 'bb', 'aa', 'cc'])}";
        top_n(..., n=2) → "{top_n(count_freq(['bb', 'aa', 'bb', 'aa', 'cc']), 2)}"
        ''')