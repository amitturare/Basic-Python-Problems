# QUESTION: 1
x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if(x == y == z):
    print("Your triangle is Equilateral.")
elif(x == y or y == z or x == z):
    print("Your triangle is Isoscles.")
elif(x**2 + y**2 == z**2 or y**2 + z**2 == x**2 or x**2 + z**2 == y**2):
    print("Your triangle is Right Angled.")
else:
    print("Your triangle is Scalene.")

# QUESTION: 2
p = float(input("Principal Amt: "))
r = float(input("Rate: "))
t = float(input("Time: "))
print("Your Simple Interest for the Provided Data = ", ((p*r*t)/1000))

# QUESTION: 3
year = int(input("Enter Year: "))
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("It's a leap year!!!")
        else:
            print("It's not a leap year!!!")
    else:
        print("It's a leap year!!!")
else:
    print("It's not a leap year!!!")


# QUESTION: 4
print("Type 1 for Addition")
print("Type 2 for Substraction")
print("Type 3 for Multiplication")
print("Type 4 for Division")
print("Type 5 for Modulus")
print("Type 6 to exit.")

while True:
    c = int(input("Enter your choice: "))
    if(c == 6):
        y = input("Want to break the loop?\n")
        if(y == "Yes"):
            a, b = None, None
            break
        else:
            continue

    a = float(input("Enter one number = "))
    b = float(input("Enter another number = "))
    
    if(c == 1):
        print('Addition of a and b = ', a + b)
    elif(c == 2):
        print('Substraction of a and b = ', a - b)
    elif(c == 3):
        print('Multiplication of a and b = ', a * b)
    elif(c == 4):
        print('Division of a and b = ', a / b)
    elif(c == 5):
        print('Modulus of a and b = ', a % b)
        