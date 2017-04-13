
import random

class Deck(object):
	def __init__(self,*arg):
		self.arg = arg


	def create_cards(self):
		suits = ["Hearts", "Spades", "Clubs", "Dimonds"]
		list_of_card = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]


		for i in range(0,len(suits)):

			print suits[i]
			for i in range (0,len(list_of_card)):
				print list_of_card[i],

	def suffle(self,num):
		rand = random.randint(1,52)
		for i in range(0,num):
			print i


		# def displayCards():




deck = Deck("spades")

deck.create_cards()
deck.suffle(2)
