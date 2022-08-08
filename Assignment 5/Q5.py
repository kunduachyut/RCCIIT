#WAP TO CALCULATE THE FACTORIAL OF A NUMBER USING FOR LOOP

a = int(input("Enter the number : "))
fact = 1
for i in range (1,a+1):
    """if(i>a):
        print(fact)
    else:"""
    fact = fact*i

print("The fantorial of ",a,"is : ",fact)