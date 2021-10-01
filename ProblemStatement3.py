# Q.1: Multiplication Table
n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(i, "x", n, "=", i * n)
    i += 1

# Q.2: Nested Loop
i = 1
while i <= 9:
    print(str(i) * i)
    i += 1

# Q.3: Sum of Natural Numbers
n = int(input("Enter a positive natural number: "))
sum = 0
while n > 0:
    sum = sum + n
    n = n - 1    
print(sum)

# Q.4: Sum of the Digits
n = int(input("Enter a number: "))
sum = 0
while i > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("Sum of digits = ",  sum)

# Q.5: Reverse Number
n = int(input("Enter a number: "))
sum = ""
while i > 0:
    digit = n % 10
    sum = sum + str(digit)
    n = n // 10
print("Sum of digits = ",  sum)

# OR
n = int(input("Enter a number: "))
a = str(n)
print(a[::-1])

