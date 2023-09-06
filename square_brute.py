#This is a brute force method to get real number square roots for any number.
#It works till you get over several billion and then it gets unbarably slow.  
#You can make this brute force work for bigger numbers by adding one if statement


#get the number you want to get the square root for.
a=int(input("Enter a number: "))

#Loop through all numbers from your number down until you find the result and stop
for x in reversed(range(2,a)):
  #if x times x = is your number 
  if (a==((a//(x*x))*(x*x))):
    #if x times x is exactly your number print x else print the rest after
    if (a/(x*x))==1:
      print (x)
    else:
      print ("{} times the square root of {}".format(x,(a/(x*x))))
    break
