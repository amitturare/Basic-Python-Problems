# Question 1
# Quadratic Equation of form = 'a'x^2 + 'b'x + 'c'

import math

def equation(a, b, c):
    d = b**2 - 4*a*c
    sqrootval = math.sqrt(d)
    root1 = ((-b + sqrootval) / 2*a)
    root2 = ((-b - sqrootval) / 2*a)

    if(d > 0):
        print("Roots are real and unequal.")
        print("Root 1 = ", root1)
        print("Root 2 = ", root2)
    elif(d == 0):
        print("Roots are same and real.")
        print("Roots are = ", -b/(2*a))
    else:
        print("Roots are complex.")
        print("Root 1 = ", (-b/(2*a)), " + i", d)
        print("Root 1 = ", (-b/(2*a)), " - i", d)

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if(a == 0):
    print("A can't be equal to 0 for a quadratic equation. Try other value.")
else:
    equation(a, b, c)

# Question 2
import random
print(random.randint(0, 100))

# Question 3
kms = float(input("Enter a value: "))
miles = (kms / 1.609)
print(miles)

# Question 4
a = int(input("Enter one number: "))

if(a > 0):
    print(a, " is a positive number.")
elif(a == 0):
    print(a, " is 0.")
else:
    print(a, " is a negative number.")