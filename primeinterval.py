num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
def primenum(num1, num2):
    for num in range(num1, num2+1):
        if num>1:
            for i in range(2, num):
                if num%i==0:
                    break;
            else:
                print(num," ")
                
result=primenum(num1, num2)




