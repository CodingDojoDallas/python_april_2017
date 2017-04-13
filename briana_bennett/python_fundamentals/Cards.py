import random

class Cards(object):
	def __init__ (self, suit, number):
		self.suit = suit
		self.number = number
		self.quantity = quantity

class Deck(object):
	def __init__ (self):
		self.deck = []
		self.create_cards()

	def create_cards(self):
	
		numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
		suits = ['heart', 'spade', 'club', 'diamond']
		cards52 = []

		for suit in suits:
			for i in range(1,14):
				if i == 1:
					i = 'A'
				elif i == 11:
					i = 'J'
				elif i == 12:
					i= 'Q'
				elif i == 13:
					i = 'K'
				cards52.append(Cards(suit, i))
		
		print cards52

		

# class Deck(cards52):

# 	def shuffle(self):
# 		print "deck has been shuffled"
# 		return self

# 	def deal(self):
# 		self.quantity -= 1
# 		return self

# 	def reset(self):
# 		self.quantity = 52
# 		return self


# class Playa(Cards):

# 	def get_cards(self):
# 		if self.quantity < 52:
# 			self.quantity += 1
# 		return self
		
		