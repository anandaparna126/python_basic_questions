print("---------MINI CALCULATOR-------")
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("enter a number between 1-4: "))

if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice ==3:
    print(num1 * num2)
else:
    print(num1/num2)

