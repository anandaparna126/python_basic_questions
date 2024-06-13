num1 = int(input("enter 1 number."))
num2 = int(input("enter 2 number."))
num3 = int(input("enter 3 number."))

def largestnum(num1, num2, num3):
    if num1>num2 & num1>num3:
        print(num1, "is the largest number.")
    elif num2>num1 & num2>num3:
        print(num2, "is the largest number.")
    else:
        print(num3, "is the largest number.")


result = largestnum(num1, num2, num3)