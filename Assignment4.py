"""
Q1 = Take input from user to make a list. 
Again take one input from user and search it in the list and delete that element, if found. iterate over list using for loop.
"""
"""
l1 = []

while True:
    n = input("Enter data to add in the list= ")
    if(n == "Done"):
        break
    else:
        l1.append(n)
        continue
print("Here is the list you created", l1)

for i in l1:
    a = input("Enter a number to check = ")
    if(a in l1):
        print(a, "is present in the list l1.")
        break
    else:
        print("Its not present.")

print("Do you want to delete any element from the list?")
yn = input()
if(yn == "yes"): 
    l1.remove(input("Type an element to delete: "))
    print("Here is the updated list:")
    print(l1)
else:
    print("Program Over!!!")
"""
"""
Q2: Take input from user to make list.
Ffrom that list containing int, float and string, make three lists to store them seperately
"""
"""
list2 = [1, 2, 3, 4, 4.8, "Hello", 7.6, 4.8]
list3 = []
list4 = []
list5 = []

for i in list2:
    if(type(i) == int):
        list3.append(i)
    elif(type(i) == float):
        list4.append(i)
    elif(type(i) == str):
        list5.append(i)

print(list3)
print(list4)
print(list5)
"""
#OR

num = int(input("Enter number of elements = "))
integers = []
floats = []
strings = []

for i in range(num):
    element = input('Enter elements: ')
    if '.' in element:
        floats.append(float(element))
    elif all([characters in  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] for characters in element]):
        integers.append(int(element))
    else:
        strings.append(element)

print('List of integers: ', end='')
print(integers)
print('List of floats: ', end='')
print(floats)
print('List of strings: ', end='')
print(strings)





