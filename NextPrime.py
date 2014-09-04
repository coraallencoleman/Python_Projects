#Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

def Prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(n**0.5)+1):
            if n % x == 0:
                return False
    return True

more = raw_input("Welcome to the prime number generator. Your first prime number is 2. Would you like another prime number? ")
n = 2
while more == "yes" or more == "YES" or more == "Yes":
    n += 1
    if Prime(n) is True:
        print "Your next prime number is " + str(n) + "."
        more = raw_input("Would you like another prime number? ")
        
else:
    print "Goodbye"