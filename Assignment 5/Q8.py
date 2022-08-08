# WAP TO DISPLAY ALL LEAP YEAR FROM  1900 - 2025 USING FOR LOOP

print("The lear year from 1900 to 2025 is -->")
n1 = 1900
n2 = 2025

for i in range (n1, n2+1):
    if(i%400==0) and (i%100==0) :
        print("This is a lear year :", i)
    elif (i%4==0) and (i%100 !=0):
        print("This is a lear year : ", i)
    else:
        print("This is not a leap year : ",i)

    
