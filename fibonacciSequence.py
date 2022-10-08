# Python Program to print Fibonacci Sequence upto n terms

n = int(input("Please enter the number of terms : "))

# Base Condition(First 2 terms)
n1, n2 = 0, 1
cnt = 0

# check if the number of terms is valid
if n <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif n == 1:
   print("Fibonacci Sequence upto ",n," :")
   print(n1)
# Generate Fibonacci Sequence
else:
   print("Fibonacci Sequence : ")
   while cnt < n:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       cnt += 1