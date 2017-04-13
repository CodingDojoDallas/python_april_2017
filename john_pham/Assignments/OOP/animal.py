class Animal(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print "Name: {}, Health: {}".format(self.name, self.health)
        return self

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        print
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()


lizard = Animal("Lizzy")
lizard.walk().walk().walk().run().run().displayHealth()

dog = Dog("Doge")
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("Draco")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
