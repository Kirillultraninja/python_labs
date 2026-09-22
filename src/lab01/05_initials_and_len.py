fio= list(map(str,input("ФИО: ").split(" ")))
b=[]
for i in fio:
    if i!= "":
        b.append(i)
print("Инициалы:",b[0][0]+b[1][0]+b[2][0])
print("Длина (символов):", len(b[0])+len(b[1])+len(b[2])+2)