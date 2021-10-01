# Question 1: Fibonacci Series 
def fib(n):
    if(n <= 1):
        return n
    else:
        return(fib(n-1) + fib(n-2))

nterms = int(input("Enter a number: "))

if(nterms <= 0):
    print("Enter a natural number.")
else:
    print("Fibonacci Sequance: ")
    for i in range(nterms):
        print(fib(i))

# OR

n = int(input("Enter a natural number: "))
a, b = 0, 1
while a < n:
    print(a)
    a, b = b, a+b

# OR

n = int(input("Enter a natural number: "))
i = 0
a, b= 0, 1

while(n > i):
    if(1 >= i):
        nxt = i
    else:
        nxt = a + b
        a = b
        b = nxt
    
    print(nxt)
    i = i + 1

# Question 3: Armstrong Number
num = int(input("Enter a number: "))
a = len(str(num))
sum = 0
i = num
while(i > 0):
    digit = i % 10
    sum = sum + digit**a
    i = i // 10

if(num == sum):
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")

# Question 2: Prime Number
num = int(input("Enter a number: "))

if(num > 0):
    for i in range(2, num):
        if(num % i == 0):
            print("Its not a prime number.")
            break
        else:
            print("Its a prime number.")
else:
    print("Its not a prime number.")
