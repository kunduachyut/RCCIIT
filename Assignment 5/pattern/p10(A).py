"""
1
12
123
1234
"""

a = int(input("Enter the number : "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")