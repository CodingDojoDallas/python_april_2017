class Bike(object):
	def __init__(self, price, max_speed, miles=0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print self.price
		print self.max_speed
		print self.miles
	
	def ride(self):
		print "riding"
		self.miles += 10
		#print self.miles
		return self

	def reverse(self):
	 	print "reversing"
	 	if self.miles >= 5:
	 		self.miles -= 5
		#print self.miles
	 	return self
	 	

bike1 = Bike(200, "25mph", 39)
bike2 = Bike(390, "20mph", 40)
bike3 = Bike(19, "4mph", 0)

# bike3
print "bike1 -------"
bike1.ride().ride().ride().reverse().displayInfo()

# bike2
print "bike2 -------"
bike2.ride().ride().reverse().reverse().displayInfo()

# bike3
print "bike3 -------"
bike3.reverse().reverse().reverse().displayInfo()
	