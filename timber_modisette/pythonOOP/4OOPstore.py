class Store(object):
	def __init__(self, location, owners_name="martin"):
		self.products = []
		self.location = location
		self.owners_name = owners_name
		
		
		
	def addProduct(self, *product):
		# listofproducts = []
		# listofproducts.append(product)
		
		for value in product:
			self.products.append(Store(value))
			#use Product instead of Store to create Product objects.
			

			
			
		





	def display(self):
		pass





this=Store("this location")

this.addProduct("tampons","razor","lipstick","almond milk", "shit", "paper towels")

# print this.products
# print this.location
	












		
