class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "Name: {}".format(self.name)
        print "Health: {}".format(self.health)
        return self


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self


class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "This is a dragon!"
        super(Dragon, self).display_health()
        return self


animal1 = Animal("George")
dog1 = Dog("Dot")
dragon1 = Dragon("Patty")
animal2 = Animal("Jorge")

for i in range(2):
    animal1.walk().run()

print "Animal1 output:\n---------------"
animal1.walk().display_health()

for i in range(2):
    dog1.walk().run()

print "\nDog1 output:\n---------------"
dog1.walk().pet().display_health()

for i in range(2):
    dragon1.walk().run().fly()

print "\nDragon1 output:\n---------------"
dragon1.walk().display_health()

print "\nAnimal2 output:\n---------------"
# animal2.pet().fly().display_health()

# dog1.fly().display_health()
