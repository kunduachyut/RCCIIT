# Write a program two numbers and find the sum , difference,production and division of two numbers

a = int(input("Enter the first number : "))
b = int(input("Enter the first number : "))

print("The sum of the two numbers are : ",(a+b))
if(a<b):
    print("The first number is smaller than the second number ")
    print("The difference of the two numbers are  : -",(b-a))
else:
    print("The difference of the two numbers are : ",(a-b))

print("The production of the two numbers are : ",(a*b))
