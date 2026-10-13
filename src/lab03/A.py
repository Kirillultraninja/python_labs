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
    return f'"{text}"'

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

    

print(rf'"ПрИвЕт\nМИр\t"',"-->",normalize("ПрИвЕт\nМИр\t"))
print(rf'"ёжик, Ёлка"  (yo2e=True) ',"-->",normalize("ёжик, Ёлка"))
print(rf'"Hello\r\nWorld"',"-->",normalize("Hello\r\nWorld"))
print(rf'"  двойные   пробелы  "',"-->",normalize("  двойные   пробелы  "))
print()
print(rf'"привет мир"',"-->",tokenize("привет мир"))
print(rf'"hello,world!!!"',"-->",tokenize("hello,world!!!"))
print(rf'"по-настоящему круто"',"-->",tokenize("по-настоящему круто")) 
print(rf'"2025 год"',"-->",tokenize("2025 год"))
print(rf'"emoji 😀 не слово"',"-->",tokenize("emoji 😀 не слово"))
print()
print("токены", str(["a","b","a","c","b","a"]),"-->","частоты",count_freq(["a","b","a","c","b","a"]))
print("токены", str(["bb","aa","bb","aa","cc"]),"-->","частоты",count_freq(["bb","aa","bb","aa","cc"]))
print()
print("top_n(count_freq("+str(["a","b","a","c","b","a"])+" 2)","-->",top_n(count_freq(["a","b","a","c","b","a"]), 2))
print("top_n(count_freq("+str(["bb","aa","bb","aa","cc"])+" 2)","-->",top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))
print()