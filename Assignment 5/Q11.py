# WAP TO CALCULATE THE SUM OF THE SERIES 1/2+2/3+...+n/(n+1) FOR LOOP 

a = int(input("Enter the number : "))
sum = 0

for i in range(1,a+1):
    div= i/i+1
    sum += div

print("The sum of the series is : ",sum)