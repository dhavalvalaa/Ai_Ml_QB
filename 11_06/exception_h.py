'''
Write a Python program that:

Asks the user to enter two numbers.

Performs division (num1 / num2).

Uses:

try to attempt execution.

except to handle errors.

else to execute when no error occurs.

finally to run cleanup code.

raise to manually raise an exception if the denominator is zero.
'''

def divisoion():
    try:
        n1 = int(input("enter the 1 number : "))
        n2 = int(input("enter the 2 number : "))

        if n2 == 0:
            raise ZeroDivisionError("cannot divide by zero")
        
        result = n1 / n2
    
    except ValueError:
        print("please enter valid numberr")

    except Exception as e:
        print("exception  is : " , e)

    else:
        print("your result is - ",result)

    finally:
        print("code ended")

divisoion()