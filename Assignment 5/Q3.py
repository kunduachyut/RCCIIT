# WAP TO PRINT ALL THE NUMBERS FROM M-N THEREBY CLASSITY THEN AS EVEN OR ODD USING FOR LOOP

print("Enter the range :")
m = int(input("Enter the first number : "))
n = int(input("Enter the second number : "))

for i in range (m,n):
    if(i%2==0):
        print("The number is even :\t",i)
    else:
        print("The number is odd :\t",i)