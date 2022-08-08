#WAP TO CALCULATE THE AVG OF N NATURAL NUMBERS USING FOR LOOP

a = int(input("Enter the number: "))
sum = 0
avg = 0

for i in range(1 , a+1):
    sum = sum+i
    avg = sum/a

print("The avg of the number is : ",avg)
