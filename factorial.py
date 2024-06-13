# num = int(input("enter a number: "))
# fact = 1
# def factorial(num):
#     if num<0:
#         print("factorial less than zero are not there")
#     elif num==0:
#         print("1")
#     if num>0:
#         for i in range(1, num+1):
#             fact = fact*i
#     print(fact)
# result = factorial(num)

## Using Recursion----------------------------------

a = int(input("enter a number: "))
def fact(a):
    if a== 0:
        return 1
    else:
        return ((a)*fact(a-1))
    
result = fact(a)
print("factorial of the given number is", result)