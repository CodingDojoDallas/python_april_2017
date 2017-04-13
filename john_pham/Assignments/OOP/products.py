class Product(object):
    def __init__(self, price, item, weight, brand, cost, status = "for sale"):
        self.price = price
        self.item_name = item
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

        # self.display_all()

    def sell(self):
        #changes status to "sold"
        self.status = "sold"
        self.display_info()
        return self

    def add_tax(self, tax):
        #takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
        totalprice = (self.price * tax) + self.price
        print totalprice
        return self

    def returnProduct(self, condition):
        #takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective change status to defective and change price to 0. If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
        if condition == "defective":
            self.status = "defective"
            self.price = 0
        if condition == "like new":
            self.status = "for sale"
        if condition == "opened":
            self.status = "used"
            self.price = self.price - (self.price * 0.20)
        return self

    def display_info(self):
        print "Price: {}, Item Name: {}, Weight: {}, Brand: {}, Cost: {}, Status: {}".format(self.price, self.item_name, self.weight, self.brand, self.cost, self.status)
        return self

horse_meat = Product(200, "Meat", "100 lb", "Racing", 100, "For Sale")
hat = Product(15, "Hat", "1 lb", "Baseball", 5, "For Sale")

horse_meat.sell()
hat.display_info()
