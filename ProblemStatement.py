# QUESTION: 1
r = float(input("Enter radius: "))
print("Area of the circle of radius ", r, "is ", 3.14 * r * r)

# QUESTION: 2
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
print("Average is = ", avg)

# QUESTION: 3
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))
if(num1>=num2 and num1>=num3):
  print(num1," is the greatest")
elif(num2>=num1 and num2>=num3):
  print(num2," is the greatest")
else:
    print(num3," is the greatest")

# QUESTION: 4
a = 10
b = 8
print(a, b)
b = a - b # b = 2, a = 10
a = a - b # a = 8, b = 2
b = a + b # a = 8, b = 10
#a, b = b, a
print(a, b)
