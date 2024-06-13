## using math module
## using exponentiation method

# ## method 1-----
# num = 64
# sq = num**(1/2)
# print("the square root of the given number is", sq)

## method 2------
import math
num1 = int(input("enter a number: "))
def sq(num1):
    sq = math.sqrt(num1)
    print("the square root of", num1, " is",sq)
    
result = sq(num1)
