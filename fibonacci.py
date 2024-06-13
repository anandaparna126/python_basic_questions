prev = 0
nxt = 1
num = int(input("enter a number: "))
print(prev)
print(nxt)
for i in range(1, num+1):
    result = prev + nxt
    prev = nxt
    nxt = result
    print(result)