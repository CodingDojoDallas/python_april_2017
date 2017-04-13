
class Animal(object):
	def __init__(self, name, health=100):
		self.name = name 
		self.health = health

	def walk(self):
		self.health-=1

	def run(self):
		self.health-=5

	def displayHealth(self):
		print "Animal Name: ",self.name
		print "Animal Health: ",self.health



