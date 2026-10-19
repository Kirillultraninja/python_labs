
from random import *
def format_record(a):
    if not isinstance(a, tuple):
        raise TypeError("Должен быть кортеж")

    if len(a) != 3:
        raise ValueError("Запись должна содержать 3 элемента")

    if not isinstance(a[0], str) or not a[0].strip():
        raise ValueError("ФИО не заполнено")

    if not isinstance(a[1], str) or not a[1].strip():
        raise ValueError("Группа не заполнена")

    if not isinstance(a[2], float):
        raise TypeError("GPA неверного типа")

    if not (0 <= a[2] <= 5.0):
        raise ValueError("GPA в неправильном диапазоне")

    s1 = a[0]
    f = 0
    iniz = ""
    s = ""
    ind1 = 0
    ind2 = len(s1)

    for i in range(len(s1) - 1):
        if s1[i] != " " and s1[i + 1] == " " and f == 0:
            f = 1
            ind2 = i + 1
        if s1[i] == " " and s1[i + 1] != " " and f == 1:
            iniz += s1[i + 1].upper() + '.'
        if s1[0] == " ":
            if s1[i] == " " and f == 0 and s1[i + 1] != " ":
                ind1 = i
        else:
            ind1 = -1

    s2 = s1[ind1 + 1].upper() + s1[ind1 + 2:ind2] + " " + iniz
    s += s2 + ', '
    s3 = "гр. " + a[1].strip() + ", "
    s += s3
    s += "GPA" + " " + f"{a[2]:.2f}"
    return s
'''a1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
a2 = ("Петров Пётр", "IKBO-12", 5.0)
a3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
a4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
test=("ываыва","","ываыва")
print(f"format_record({a1}) -->", format_record(a1))
print(f"format_record({a2}) -->", format_record(a2))
print(f"format_record({a3}) -->", format_record(a3))
print(f"format_record({a4}) -->", format_record(a4))
print(f"format_record({test}) -->", format_record(test))'''

print(2608518%15 +1)