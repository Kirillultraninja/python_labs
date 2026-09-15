a= input("a: ")
b= input("b: ")
a1= float(a[0]+"."+a[2:])
b1= float(b[0]+"."+b[2:])
sum=a1+b1
avg= round(sum/2,2)
print(f"sum={sum};",f"avg={avg}")