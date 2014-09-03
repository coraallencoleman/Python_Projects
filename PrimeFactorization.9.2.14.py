#Prime Factorization - Have the user enter a number and find all prime factors (if there are any) and display them

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

def FindFactors(n):
    factors = [] 
    for x in range(1, n+1):
        if n % x == 0:
            factors.append(x)
    return factors
        
UserNumber = abs(int(raw_input("Please enter a number to get its Prime Factors ")))

#Find factors then test each factor for primality
PrimeFactors = []
factors = FindFactors(UserNumber)
for x in factors:
    if Prime(x) == True:
        PrimeFactors.append(x)
print PrimeFactors