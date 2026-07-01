#Bike rental project
class Bikeshop:
    def __init__(self, stock):  # fixed typo
        self.stock = stock

    def displayBike(self):
        print("We have", self.stock, "bikes in stock")
        print("one bike is rented for 500 rupes per day")

    def rentforBike(self, q):
        if q <= 0:
            print("Please enter a positive number")
        elif q > self.stock:
            print("Sorry! We have only", self.stock, "bikes in stock")
        else:
            self.stock -= q
            print("You have rented", q, "bikes. Now we have", self.stock, "bikes in stock")

    def returnBike(self, q):
        if q <= 0:
            print("Please enter a positive number")
        else:
            self.stock += q
            print("You have returned", q, "bikes. Now we have", self.stock, "bikes in stock")


shop = Bikeshop(100)  # moved outside the loop

while True:
    input1 = int(input("Enter 1 to display bikes\nEnter 2 to rent\nEnter 3 to return\nEnter 4 to exit\n"))
    if input1 == 1:
        shop.displayBike()
    elif input1 == 2:
        q = int(input("Enter the number of bikes you want to rent: "))
        shop.rentforBike(q)
        Rs = q * 500
        print("You have to pay", Rs, "rupes for renting", q, "bikes and 2000 rupes as security deposit and you will get it back when you return the bikes")
    elif input1 == 3:
        q = int(input("Enter the number of bikes you want to return: "))
        shop.returnBike(q)
    elif input1 == 4:
        break