# declare a class and give it name User
class Bike(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.miles
        print self.max_speed
        return self

    def ride(self):
        print 'Riding'
        self.miles = self.miles + 10
        return self

    def reverse(self):
        print 'Reversing'
        self.miles = self.miles - 5
        if self.miles < 0:
            self.miles = 0
        return self

#now create an instance of the class
mongoose = Bike(400, 20, 5)
for i in range(3):
    mongoose.ride()
mongoose.reverse()
mongoose.displayInfo()

# mongoose.ride().reverse()
