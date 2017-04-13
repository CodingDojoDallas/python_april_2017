

class Bike(object):

	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print "The price: {}".format(self.price)
		print "The max_speed: {}".format(self.max_speed)
		print self.miles

	# def ride(self,num):
	# 	print "riding"*num
	# 	self.miles = self.miles+(10*num)

	def ride(self):
		print "riding"
		self.miles+=10


	# def reverse(self,num):
	# 	print "reversing"*num
	# 	self.miles =self.miles - (5*num)
	# 	if self.miles<0:
	# 		self.miles=0

	def reverse(self):
		print "reversing"
		self.miles-=5
		if self.miles<0:
			self.miles=0



bike1 = Bike(200, "25mph",100)
for i in range(0,3):
	bike1.ride()
bike1.reverse()
bike1.displayInfo()

print "\n\n"

bike2 = Bike(300, "27mph",110)
for i in range(0,2):
	bike2.ride()

for i in range(0,2):
	bike2.reverse()

bike2.displayInfo()

print "\n\n"

bike3 = Bike(400, "28mph",150)
for i in range(0,3):
	bike3.reverse()
bike3.displayInfo()


