num = int(input("enter a number: "))
def nat_num(num):
    if num<=1:
        return num
    else:
        return ((num) + nat_num(num-1))
    
result = nat_num(num)
print(result)