class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self
    def displayinfo(self):
        print "Price: {}, Maximum speed: {}. Total miles: {}".format(self.price, self.max_speed, self.miles)
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "35mph")
bike3 = Bike(400, "45mph")

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
