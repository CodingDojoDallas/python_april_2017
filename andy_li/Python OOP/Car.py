class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if price > 10000:
            self.tax += 0.03

        self.display_all()

    def display_all(self):
        print "Price: ${}".format(self.price)
        print "Speed: {} mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {} mpg".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self

print "Car1 info\n---------------"
car1 = Car(2000, "35", "Full", 15)
print "\nCar2 info\n---------------"
car2 = Car(2067, "56", "Empty", 67)
print "\nCar3 info\n---------------"
car3 = Car(203, "87", "Half full", 800)
print "\nCar4 info\n---------------"
car4 = Car(10001, "2", "Full", 25)
print "\nCar5 info\n---------------"
car5 = Car(2002, "90", "Kind of full", 19)
print "\nCar6 info\n---------------"
car6 = Car(2001, "100000", "Running on fumes", 6)
