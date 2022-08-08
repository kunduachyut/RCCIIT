# WAP TO CALCULATE THE SUM OF CUBES OF NUMBERS FROM 1-n USING FOR LOOP 

a = int(input("Enter the number : "))
sum = 0

for i in range (1,a+1):
    sum += pow(i,3)

print("The sum of the cubic number is : ",sum)