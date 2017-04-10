class Product(object):
	def __init__(self, price, item_name, weight, brand, cost, status="for sale"):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status
	def sell(self):
		self.status = "sold"
		return self
	def addTax(self,tax):
		self.cost = self.price + (self.price * tax)
		return self
	def returns(self,returnForm):
		#self.status = returnForm
		if returnForm == "defective":
			self.price = 0 
			self.status = "defective"
			return self
		if returnForm == "in box":
			self.status = "for sale"
			return self
		if returnForm == "open box":
			self.status = "used"
			self.price = self.price - (self.price * .20)
			return self
	def displayInfo(self):
		print "price:{} Item:{} weight:{} brand: {} cost:{} status: {}".format(self.price, self.item_name, self.weight, self.brand, self.cost, self.status)

radio = Product(10.00, "radio", 10, "samsung", 10.00,)

radio.sell().addTax(.08).returns("defective").displayInfo()

