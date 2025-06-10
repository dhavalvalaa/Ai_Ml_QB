class atm:
    counter = 0

    def __init__(self,acno,amount):
        self.acno = acno
        self.amount = amount
        atm.counter = atm.counter + 1

    def pinc(self,num):
        self.__num = num

    def get_pin(self):
        return self.__num
    
    def set_pin(self):
        self.__num = input("create  pin = ")

    def deposit(self,price):
        self.amount += price

    def withdraw(self,price):
        if self.__num == input("enter pin = "):
            self.amount -= price
        else:
            print("invalid pin! please try again")

    def display(self):
        print("your balance = ", self.amount)
        
