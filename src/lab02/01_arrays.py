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
def unique_sorted(nach,kon,a):
    L=nach 
    R=kon
    if L>R: return a
    x= a[(L+R)//2]
    while L<=R:    
        while L<kon and a[L]<x:
            L+=1
        while R>nach and a[R]>x:
            R-=1
        if L<=R:
            a[L],a[R] = a[R],a[L]
            L+=1
            R-=1
    unique_sorted(nach,R,a)
    unique_sorted(L,kon,a)
    return a
a1= [3, -1, 5, 5, 0]
a2= [42]
a3= [-5, -2, -9]
a4= []
a5= [1.5, 2, 2.0, -3.1] 
a6= [3, 1, 2, 1, 3]
a8= [-1, -1, 0, 2, 2]
a9= [1.0, 1, 2.5, 2.5, 0]
m1=list(set(a6))
m2=list(set(a4))
m3=list(set(a8))
m4=list(set(a9))
#print(f"{a1} --> ", min_max(a1))
#print(f"{a2} --> ", min_max(a2))
#print(f"{a3} --> ", min_max(a3))
#print(f"{a4} --> ", min_max(a4))
#print(f"{a5} --> ", min_max(a5))
print(f"{a6} -->", unique_sorted(0,len(m1)-1,m1))
print(f"{a4} -->", unique_sorted(0,len(m2)-1,m2))
print(f"{a8} -->", unique_sorted(0,len(m3)-1,m3))
print(f"{a9} -->", unique_sorted(0,len(m4)-1,m4))
