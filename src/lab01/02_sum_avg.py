a=input("a: ")
b=input("b: ")
if "," in a:
    a1=list(map(str, a.split(',')))
    a2= float(str(a1[0])+"."+str(a1[1]))
else:
    a2=float(a)
if "," in b:    
    b1=list(map(str, b.split(',')))
    b2= float(str(b1[0])+"."+str(b1[1]))
else:
    b2=float(b)
sum=a2+b2
avg= round(sum/2,2)
print(f"sum={sum};",f"avg={avg}")