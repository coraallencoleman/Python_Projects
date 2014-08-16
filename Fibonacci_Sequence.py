#Fibonacci Sequence - Enter a number and have the 
#program generate the Fibonacci sequence to that number or to the Nth number.
n = 0
plus1 = 1

length = raw_input("How many numbers would you like in your Fibonacci Sequence? ")

if length == 1:
    FibList = [0]
elif length == 2:
    FibList = [0, 1]
else:
    FibList = [0, 1]
    for l in range(int(length) - 2):
        new = int(n) + int(plus1)
        n = int(plus1)
        plus1 = new
        FibList.append(new)

print FibList

