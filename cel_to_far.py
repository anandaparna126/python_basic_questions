C = int(input("enter celcius: "))
def cel_to_far(C):
    F = (C * (9/5)) + 32
    print(C, "celcius", "means", F,"Fahrenheit.")

result = cel_to_far(C)