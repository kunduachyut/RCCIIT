"""
1
22
333
4444
55555
"""

a = int(input("Enter the number : "))
for i in range(a+1):
    for j in range(i):
        print(i,end=" ")
    print("\n")