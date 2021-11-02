number = input ("Enter number\n")
try:
    val = int(number)
    print("Yes input string is an Integer.")
except ValueError:
    print("That's not an int!")

if val > 1:
    for i in range(2,val):
        if (val % i) == 0:
            print("El número no es primo")
            break
    else:
        print("El número es primo!")

else:
    print("El número no es primo")

