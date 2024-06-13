x= int(input("enter first number: "))
y= int(input("enter second number: "))
def Hcfactor(x,y):
    if x<y:
        smaller=x
    else:
        smaller = y
        
    for i in range(1, smaller+1):
        if((x%i==0) and (y%i==0)):
            Hcf = i
    print("HCF:", Hcf)
    
result = Hcfactor(x,y)