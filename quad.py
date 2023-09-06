#i# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath as math
#import math

a =float(input("enter a:  "))
b =float(input("enter b:  "))
c =float(input("enter c:  "))

# calculate the discriminant
d = (b**2) - (4*a*c)
#print ("des = {}".format( d))

#print ("p2 ={} ".format(2*a))

#print ("sqrt =  {}".format(math.sqrt(d)))



# find two solutions
sol1 = (-b-math.sqrt(d))/(2*a)
sol2 = (-b+math.sqrt(d))/(2*a)

print('The solution are:\n x= {0}\nx= {1}'.format(sol1,sol2))
