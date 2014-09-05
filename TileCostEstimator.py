#Find Cost of Tile to Cover W x H Floor - 
#Calculate the total cost of tile it would take to cover a floor plan of 
#width and height, using a cost entered by the user.
 
cost = float(raw_input("Please enter cost of the tile per square inch in dollars: ").translate(None, "$"))
 
width_input = raw_input("Please enter the dimensions of your surface in inches (W x H): ")
 
width = []
for t in width_input.split():
    try:
        width.append(float(t))
    except ValueError:
        pass
 
area = width[0]*width[1]
estimate = area*cost
estimate = "%0.2f" % estimate
print "The cost estimate for tile to cover your floor is $" + str(estimate) + "."