n=int(input("in_1: "))
k1=0
k2=0
for i in range(n):
    a=input(f"in_{i+2}: ")
    if "True" in a:
        k1+=1
    elif "False" in a:
        k2+=1
print("out:",k1,k2)
