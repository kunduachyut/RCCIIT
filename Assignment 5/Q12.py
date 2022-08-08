# WAP TO CALCULATE THE SUM OF THE SERIES 1/1+2^2/2+...+n^2/n FOR LOOP

a = int(input("Enter the number : "))
sum = 0

for i in range(1,a+1):
    power = pow(i,2)
    div = power/i
    sum += div

print("The sum of the series is : ",sum)