#Change Return Program - The user enters a cost and then the amount of money given. 
#The program will figure out the change and the number of quarters, dimes, 
#nickels, pennies needed for the change.

cost = float(raw_input("What is the cost of your item? "))
payment = float(raw_input("How much was paid? "))

difference = payment - cost
print difference

while difference < 0:
    payment = float(raw_input("The customer did not pay enough. Please re-enter payment amount"))
    difference = payment - cost

tens = 0
fives = 0
ones = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while difference/10 > 1:
    tens = int(difference/10)
    difference -= 10*tens

while difference/5 > 1:
    fives= int(difference/5)
    difference -= 5*fives


while difference/1 > 1:
    ones = int(difference/1)
    difference -= ones
    
while difference/.25 > 1:
    quarters = int(difference/.25)
    difference -= quarters*.25

while difference/.10 > 1:
    dimes = int(difference/.10)
    difference -= dimes*.10
    
while difference/.05 > 1:
    nickels = int(difference/.05)
    difference -= nickels*.05
    
while difference/.01 > 1:
    pennies = int(difference/.01)
    difference -= pennies*.01

print "The changes due is " + str(tens) + " tens, " + str(fives) + " fives, " + str(ones) + " ones, " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickels) + " nickels, and " + str(pennies) + " pennies."