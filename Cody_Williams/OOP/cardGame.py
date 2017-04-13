import random

class Card(object):
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class Deck(object):
	def __init__(self):
		#build the deck of card objects
		self.deck = []
		self.reset()
		self.shuffle()

	def reset(self):
		self.deck = []
		suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
		for suit in suits:
			for i in range(2, 15):
				value = i
				if i == 11:
					value = 'Jack'
				elif i == 12:
					value = 'Queen'
				elif i == 13:
					value = 'King'
				elif i == 14:
					value = 'Ace'
				self.deck.append(Card(suit, value))

	def display(self):
		for card in self.deck:
			print "{} of {}".format(card.value, card.suit)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self, num, players):
		if type(players) is Player:
			players = [players]
		for player in players:
			for i in range(num):
				player.hand.append(self.deck.pop())

class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []



deck = Deck()

cody = Player('Cody')
dave = Player('Dave')
bob = Player('Bob')

players = [cody, dave, bob]

deck.deal(2, cody)

print cody.hand

# print "There are {} cards in the deck".format(len(deck.deck))

# for player in players:
# 	print '*' * 20
# 	print "{}'s hand:".format(player.name)
# 	for card in player.hand:
# 		print "{} of {}".format(card.value, card.suit)

# print cody.name









