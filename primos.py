number = input ("Enter number\n")
try:
    val = int(number)
    print("Yes input string is an Integer.")
except ValueError:
    print("That's not an int!")

primo = val%2
if val == 2:
    print("El 2 es un numero primo")
elif primo == 0:
   print("El numero no es primo")
else:
 print("El numero es primo!")
