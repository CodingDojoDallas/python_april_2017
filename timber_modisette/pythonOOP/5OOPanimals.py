class Animals(object):
	def __init__(self, name, health=100):
		self.name = name
		self.health = health

	def walk(self,num):
		print "walking " *num
		self.health = self.health - (1 * num)
		return self

	def run(self,num):
		print "running " * num
		self.health = self.health - (5 * num)
		return self

	def displayHealth(self):
		print "animal name is {}. Health is {}".format(self.name,self.health)


cat = Animals("rufus")

cat.walk(3).run(2).displayHealth()





class Dog(Animals):
	def __init__(self, name, health=150):
		super(Dog,self).__init__(name, health)

	def pet(self,num):
		print "peting" * num
		self.health = self.health + (5 * num)
		return self





chow = Dog("boob")
chow.walk(3).run(1).pet(1).displayHealth()


class Dragon(Animals):
	def __init__(self, name, health=170):
		super(Dragon, self).__init__(name, health)
		

	def flying(self, num):
		print "flying " * num
		self.health = self.health - (10 * num)
		return self

	def displayHealth(self):
		print "Im a dragon"
		super(Dragon, self).displayHealth()


fire = Dragon("smokey")

fire.walk(3).run(2).flying(2).displayHealth()

