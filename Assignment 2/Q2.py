# to swap two numbers

a = int(input("Enter the first number : "))
b = int(input("Enter the first number : "))
print ("Before",a,",",b)
a = a + b
b = a - b
a = a - b

print("after",a,",",b)