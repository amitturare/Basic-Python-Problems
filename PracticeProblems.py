# Quesiton 1
i = 1
while(i <= 5):
    print("Hello World!!!")
    i = i + 1
print("While Loop Over")

# Question 2 
i = 1 
while(i <= 10):
    print(i)
    i = i + 1
print("Done!!!")

# Question 3: Factorial
def factorial(num):
    if(num == 1):
        return num
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))

if(num < 0):
    print("Enter a natural number.")
elif(num == 0):
    print("Factorial of 0 is 1.")
else:
    print("Factorial of", num, "is: ", factorial(num))

