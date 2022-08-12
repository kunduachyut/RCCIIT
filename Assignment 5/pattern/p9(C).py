a =int(input("Enter the row number :")) 
b = 2*a -2
for i in range (0,a):
    for j in range(0,b):
        print(end=" ")
    b -= 1
    for j in range(0,i+1): 
        print("* ",end=" ")
    print("")
    b = a -2
for i in range (a,-1,-1):
    for j in range(b,0,-1):
        print(end=" ")
    b+=1
    for j in range(0,i+1):
        print("* ",end=" ")
    print("")