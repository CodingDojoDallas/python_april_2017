class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status = "For sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.price = self.price * (1 + tax)
        return self

    def modify_status(self, status, price):
        self.status = status
        self.price = price
        return self

    def return_reason(self, reason):
        reasons = {
            "defective" : ["defective", 0],
            "box, like new" : [self.status, self.price],
            "opened" : ["used", (self.price * 0.80)]
        }

        values = reasons.get(reason, "Invalid return reason.")
        self.modify_status(values[0], values[1])
        return self

    def display_info(self):
        print "Price: {}".format(self.price)
        print "Item name: {}".format(self.item_name)
        print "Weight: {}".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Cost: {}".format(self.cost)
        print "Status: {}".format(self.status)

product1 = Product(1, 2, 3, 4, 5)
# product1.display_info()
# product1.sell().display_info()
# product1.add_tax(0.25).display_info()
product1.return_reason("box, like new").display_info()
