class Product(object):
    def __init__(self, price, item_name, weight, brand, cost, status = 'for sale'):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        self.status = 'sold'
        return self

    def add_tax(self, tax):
        self.price = self.price + (self.price * tax)
        return self

    def returned(self, reason):
        if reason == 'defective':
            self.status = 'defective'
            self.price = 0
        elif reason == 'in box':
            self.status = 'like_new'
        elif reason == 'opened':
            self.status = 'used'
            self.price = self.price - (self.price * .20)
        return self

    def displayAll(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.cost
        print self.status
        # return self


apple = Product(1200, 'TV', 3, 'nice', 'money', 'good').add_tax(.092).displayAll()
