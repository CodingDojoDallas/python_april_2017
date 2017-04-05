class Car(object):
    def __init__(self, price, speed, fuel, mileage):

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = .12
        if self.price > 10000:
            self.tax = .15
        self.displayAll()
    def displayAll(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax


mustang = Car(30000,400,18,1000)
audi = Car(70000, 600, 21, 29)
tesla = Car(120000, 1000, 'none', 350)
honda = Car(9999, 160, 40, 100000)
BMW = Car(60000, 300, 25, 1200)
mazerati = Car(140000, 500, 20, 23000)
