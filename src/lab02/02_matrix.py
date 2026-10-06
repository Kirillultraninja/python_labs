def proverka(a):
    m=set()
    for i in a:
        m.add(len(i))
    return len(m)
def transpose(a):
    f=proverka(a)
    if f==1:
        stroky=[]
        for i in range(len(a[0])):
            stroky.append(["x"]*len(a))
        for i in range(len(stroky)):
            for j in range(len(stroky[i])):
                stroky[i][j] = a[j][i]
        return stroky
    else:
        if f==0:
            return a
        else:
            return ValueError("ValueError (Рваная матрица)")
def row_sums(a):
    f=proverka(a)
    if f==1:
        b=[sum(i) for i in a]
        return b
    else:
        if f==0:
            return a
        else:
            return ValueError("ValueError (Рваная матрица)")
def col_sums(a):
    f=proverka(a)
    if f==1:
        b=[0]*len(a[0])
        for i in range(len(a)):
            for j in range(len(a[i])):
                b[j]+= a[i][j]
        return b
    else:
        if f==0:
            return a
        else:
            return ValueError("ValueError (Рваная матрица)")
a1 = [[1, 2, 3]]
a2 = [[1], [2], [3]]
a3 = [[1, 2], [3, 4]]
a4 = []
a5 = [[1, 2], [3]]
b1 = [[1, 2, 3], [4, 5, 6]]
b2 = [[-1, 1], [10, -10]]
b3 = [[0, 0], [0, 0]]
b4 = [[1, 2], [3]]
c1 = [[1, 2, 3], [4, 5, 6]]
c2 = [[-1, 1], [10, -10]]
c3 = [[0, 0], [0, 0]]
c4 = [[1, 2], [3]]
print("transpose")
print(f"transpose({a1}) -->", transpose(a1))
print(f"transpose({a2}) -->", transpose(a2))
print(f"transpose({a3}) -->", transpose(a3))
print(f"transpose({a4}) -->", transpose(a4))
print(f"transpose({a5}) -->", transpose(a5))
print("row_sums")
print(f"row_sums({b1}) -->",row_sums(b1))
print(f"row_sums({b2}) -->",row_sums(b2))
print(f"row_sums({b3}) -->",row_sums(b3))
print(f"row_sums({b4}) -->",row_sums(b4))
print("col_sums")
print(f"col_sums({c1}) -->",col_sums(c1))
print(f"col_sums({c2}) -->",col_sums(c2))
print(f"col_sums({c3}) -->",col_sums(c3))
print(f"col_sums({c4}) -->",col_sums(c4))


