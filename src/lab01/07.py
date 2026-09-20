s = input("in: ")
b=''
fl=0
p=0
shag=-1
for i in range(len(s)):
    if s[i]!=" ":
        if s[i].isupper()==True and fl==0:
            b+=s[i]
            ind1=i
            fl=1
        if s[i] in "0123456789" and fl==1 and p==0:
            ind2=i+1
            p=1
            b+=s[i+1]
            shag = ind2-ind1
    if shag!=-1:
        if ind2+shag==i:
            b+=s[i]
            ind2=i
print("out:", b)
    
        
        
        
