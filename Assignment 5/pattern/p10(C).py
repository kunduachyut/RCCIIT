"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""
a = int(input("Enter the number : "))
for i in range(1,a+1):
    num = 1
    for j in range(a,0,-1):
        if(j>i):
            print(" ",end=" ")
        else:
            print(num,end=" ")
            
            num +=1
    print("\n")