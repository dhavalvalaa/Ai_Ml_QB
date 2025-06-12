# Write a function that calculates the factorial of a number and demonstrate calling it in
# a main program

def fact(n):
    if n in (0,1):
        return 1
    elif n <0:
        print("invalid nuember")
    else:
        return n * fact(n-1)
    
print(fact(int(input("enter number = "))))