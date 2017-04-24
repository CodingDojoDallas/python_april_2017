class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Max speed:", str(self.max_speed)
        print "Mileage:", str(self.miles), "miles"
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(100, "30 mph")
bike2 = Bike(150, "40 mph")
bike3 = Bike(200, "50 mph")

print "Bike1 in action!\n----------------"
for i in range(3):
    bike1.ride()

bike1.reverse().displayInfo()

print "\nBike2 in action!\n----------------"
for i in range(2):
    bike2.ride()
    bike2.reverse()

bike2.displayInfo()

print "\nBike3 in action!\n----------------"
for i in range(3):
    bike3.reverse()

bike3.displayInfo()
