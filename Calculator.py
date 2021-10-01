'''
a = float(input("Enter one number"))
b = float(input("Enter another number"))

print("Print 1 for Addition")
print("Print 2 for Substraction")
print("Print 3 for Multiplication")
print("Print 4 for Division")
print("Print 5 for Modulus")

try:
    c = int(input("Enter your choice: "))
    
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
except:
    print("Enter the number from the following above.")
'''

#OR

def calc(a,b):
        print("Type 1 for Addition\nType 2 for Substraction\nType 3 for Multiplication\nType 4 for Division\nType 5 for Modulus\nType 6 to Exit")

        while True:
        
            c = int(input("Enter your choice: "))
        
            if(c == 1):
                print('Addition of a and b =', a + b)
            elif(c == 2):
                print('Substraction of a and b =', a - b)
            elif(c == 3):
                print('Multiplication of a and b =', a * b)
            elif(c == 4):
                print('Division of a and b =', a / b)
            elif(c == 5):
                print('Modulus of a and b =', a % b)
            elif(c == 6):
                d = input('Do you want to continue? ')
                if d == 'yes':
                    a = float(input("Enter one number: "))
                    b = float(input("Enter another number: "))
                    continue
                else:
                    break

a = float(input("Enter one number: "))
b = float(input("Enter another number: "))
calc(a,b)