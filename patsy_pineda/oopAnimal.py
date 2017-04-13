class Animal(object):
	def __init__(self, name, health=100):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def displayHealth(self):
		print "Name:{} Health: {}".format(self.name, self.health)

class Dog(Animal):
	def __init__(self, name, health = 150):
		super(Dog, self).__init__(name, health)
		self.health = health
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self, name, health = 170):
		super(Dragon, self).__init__(name, health)
		self.health = health
	def displayHealth(self):
		print "This is a dragon"
		super(Dragon, self).displayHealth()
	def fly(self):
		self.health -= 10
		return self


dog = Animal("Dugg")
dog.walk().walk().walk().run().run().displayHealth()

charlie = Dog("Charlie")
charlie.walk().walk().walk().run().run().pet().displayHealth()

emily = Dragon("Emily")
emily.walk().walk().walk().run().run().fly().fly().displayHealth()