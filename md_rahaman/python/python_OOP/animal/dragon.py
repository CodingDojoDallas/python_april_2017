
from animal import Animal

class Dragon(Animal):
	def __init__(self, name):
		super(Dragon,self).__init__(name)
		self.health = 170

		return self

	def fly(self):
		self.health -=10

		return self

	def displayHealth(self):
		print "This is dragoon"
		super(Dragon,self).displayHealth()
