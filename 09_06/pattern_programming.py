'''
Enter the row size for the pattern: 5
* 
* * 
* * * 
* * * * 
* * * * * 

=== Code Execution Successful ===
'''
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end="  ")
    for j in range(i+1):
        print("*", end = "  ")
    for j in range(i):
        print("*",end="  ")
    print()
for i in range(n,-1,-1):
    for j in range(i,n):
        print(" ", end="  ")
    for j in range(i+1):
        print("*", end = "  ")
    for j in range(i):
        print("*",end="  ")
    print()
