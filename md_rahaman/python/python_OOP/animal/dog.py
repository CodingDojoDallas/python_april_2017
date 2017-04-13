from animal import Animal

class Dog(Animal):
	def __init__(self, name):
		super(Dog,self).__init__(name)
		self.health=150

	def pet(self):
		self.health+=5

