# : Create a basic calculator that can perform addition, subtraction, multiplication, and
# division.

class basic_cal:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def addi(self):
        print("aadddition : ",end=" ")
        return self.n1 + self.n2
    def sub(self):
        print("subtraction = ",end=" ")
        return self.n1 - self.n2
    def mul(self):
        print("multification = ",end=" ")
        return self.n1 * self.n2
    def divi(self):
        try:
            print("divistion", end=" ")
            return self.n1 / self.n2
        except Exception as e:
            print(e)

n1 = int(input("enter n1 number = "))
n2 = int(input("enter n2 number = "))

ob1 = basic_cal(n1,n2)
print(ob1.addi())
print(ob1.mul())
print(ob1.sub())
print(ob1.divi())