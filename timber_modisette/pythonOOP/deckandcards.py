import random 

class Card(object):
	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

	def display(self):
		print "{} of {}".format(self.suit,self.number)


class Deck(object):
	def __init__(self):
		self.cards =[]
		self.build()

	def build(self):
		for s in ["Hearts", "Diamonds", "Clubs", "Spades"]:
			for v in range(1,14):
				self.cards.append(Card(v,s))
					
	def show(self):
		for card in self.cards:
			card.display()


deck = Deck()



deck.show()
