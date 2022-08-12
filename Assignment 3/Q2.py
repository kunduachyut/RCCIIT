# write a program to find the maximum value among three numbers

a = int(input("1st number: "))
b = int(input("2nd number:"))
c = int(input("3rd number:"))

if(a>b and a>c):
    print(a,"is maximum value ")
elif(b>a and b>c):
    print(b,"is maximum value ")
else:
    print(c,"is maximum value ")
