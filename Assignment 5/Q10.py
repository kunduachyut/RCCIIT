# WAP TO CALCULATE THE SUM OF THE SERIES 1/1^2+1/2^2+1/3^2+...+1/N^2

a = int(input("Enter the number : "))
sum = 0

for i in range(1,a+1):
    power = pow(i,2) 
    div= 1/power
    sum += div

print("The sum of the series is : ",sum)