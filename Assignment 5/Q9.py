# WAP TO CALCULATE THE SUM OF THE SERIES 1/1+1/2+1/3+...+1/N
a = int(input("Enter the number : "))
sum = 0

for i in range(1,a+1):
    div= 1/i
    sum += div

print("The sum of the series is : ",sum)