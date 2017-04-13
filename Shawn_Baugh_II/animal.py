class Animal(object):
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def walk(self):
        self.health = self.health - 1
        return self
    def run(self):
        self.health = self.health - 5
        return self
    def displayHealth(self):
        print self.name
        print self.health
        return self

snake = Animal('snake').walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health = self.health + 5
        return self
yea = Dog('scooter').walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
    def __init__(self, name, health = 170):
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health = self.health - 10
        return self

    def displayHealth(self):
        print 'This a Dragon bruh. Fire fire, flame flame!!'
        super(Dragon, self).displayHealth()
        return self

toasty = Dragon('toasty').walk().walk().walk().run().run().fly().fly().displayHealth()
