def min_max(a):
    if len(a)==0:
        return "ValueError"
    else:
        ma=a[0]
        mi=a[0]
        for i in a:
            if i>ma:
                ma=i
            if i<mi:
                mi=i
        return (mi,ma)
a1= [3, -1, 5, 5, 0]
a2= [42]
a3= [-5, -2, -9]
a4= []
a5= [1.5, 2, 2.0, -3.1] 
print(f"{a1} --> ", min_max(a1))
print(f"{a2} --> ", min_max(a2))
print(f"{a3} --> ", min_max(a3))
print(f"{a4} --> ", min_max(a4))
print(f"{a5} --> ", min_max(a5))
