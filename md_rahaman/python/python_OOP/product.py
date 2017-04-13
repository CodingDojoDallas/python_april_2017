

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

	def add_tax(self, tax_rate):
		self.price = tax_rate*self.price+self.price
		return self

	def return_iteam(self, reason):
		if(reason == "defective"):
			self.status = "defective"
			self.price = 0
		if(reason == "like new"):
			self.status = "for sale"
		if(reason == "used"):
			self.status = "used"
			self.price = self.price - (0.2*self.price)
		return self

	def display_info(self):
		print "Price: ",self.price
		print "Item Name: ",self.item_name
		print "Weight: ",self.weight
		print "Brand: ",self.brand
		print "Cost: ",self.cost
		print "Status: ",self.status

		return self


product1=Product(100,"candy bar","12g","Snekers",100)
product1.add_tax(0.12)
product1.return_iteam("defective")
product1.display_info()



