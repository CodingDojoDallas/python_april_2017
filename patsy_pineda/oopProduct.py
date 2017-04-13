class Product(object):
	def __init__(self, price, itemName, weight, brand, cost, reasonStatus, status = "for sale"):
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = status
		self.displayinfo()
	def sell(self):
		self.status = "sold"
		self.displayinfo()
		return self
	def addTax(self, tax):
		totalprice = (tax*self.price) + self.price
		print totalprice
		return self
	def returnProduct(self, reason):
		if reasonStatus == "Defective":
			self.status = "Defective"
			self.price = 0
		if reasonStatus == "Like new":
			self.status = "For sale"
		if reasonStatus == "Opened":
			self.status = "Used"
			self.price = self.price -(self.price * .20)
		return self

	def displayinfo(self):
		print "Price: ${}  Item Name: {}  Weight: {}  Brand: {}  Cost: ${}  Status:{}".format(self.price, self.itemName, self.weight, self.brand, self.cost, self.status)
		return self

hat = Product(100, "Hat", "200g", "Coach", 50, "Like new")
hat.addTax(.08)
hat.sell()
