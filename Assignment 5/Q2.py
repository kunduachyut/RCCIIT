# WAP TO PRINT THE MULTIPLICATION TABLE OF N WHERE N IS ENTERED BT THE USER USING FOR LOOP

a = int(input("Enter the number : "))
multi = 1
print("The multiplication table for",a,"is :")
for i in range(1,11):
    multi = a*i
    print(a,"*",i,"=",multi)