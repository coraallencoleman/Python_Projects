'''
Find PI to the Nth Digit - Enter a number 
and have the program generate PI up to 
that many decimal places. Keep a limit to how far the program will go.
'''
pi = "3.1415926535"

d = 0
d = raw_input("How much pi would you like?")

if d >= 0 and d < 10:
    print "The limit is 10 digits. Please pick a number between 0 and 10"
else:
    print pi[:int(d)+2]
  