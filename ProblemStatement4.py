#Q1: Accept string “geekforgeek” from user. Print all letters of the given string except e and s.
#Input: geeksforgeeks 
"""
string = input("Enter a string: ")
for i in string:
    if not i == 'e' and not i == 's':
        print("Output Letter:", i)
"""

# Q2: Program to print squares of all numbers present in a list. 
"""
l1 = []

while True:
    abc = input("Enter numbers to add in the list: ")
    if(abc == "Done"):
        break
    else:
        l1.append(abc)
        continue
print("Here is the list you created", l1)

print("Here are the squares of of all the numbers present in the list -")
for i in l1:
    a = int(i)
    print(a**2, end=" ")
"""

# Q3: Program to print the sum of first 5 natural numbers(use range function)
"""
sum = 0
for i in range(1, 6):
    sum += i
print("Total Sum =", sum)
"""

#Q4: Write a python program to print largest number from the list. 
#list=[1,2,3,4,5] 
#Expected Output: 5
"""
list1 = [1, 2, 3, 4, 5]
print(max(list1)
"""

# Q5: Python Program to Replace all Occurrences of ‘a’ with $ in a String
"""
x = input("Enter a string: ")
y = n.replace('a', '$')
y = n.replace('A', '$')
print("Modified String:", y)
"""

# Q6: This is a Python Program to count the number of vowels in a string
"""
string = input("Enter string:")
vowels = 0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)
"""

