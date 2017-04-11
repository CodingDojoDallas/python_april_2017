# -*- coding: utf-8 -*-
"""
Python Algorithm Assignment

Author: Jason Lee

"""

import math

def change(cents):
	### create coin list to return and coin to denominate with.
	coins = {}
	# coin={'dollar':1.0,'half-dollar':0.5, 'quarter':0.25, 'dime':0.10,'nickel':0.05,'penny':0.01}
	# print coin['penny']	
	
	### calculate numbers of each coin in cents.
	# for type_of_coin in coin.keys():
	# 	coins[type_of_coin]=math.floor(cents/coin[type_of_coin])
	# 	cents=cents%coin[type_of_coin]
	# return coins
	#<-------- Does not work due to unordered element characteristic of dictionary

# 	print coin.items()
# change(10)
#<------ produce list of tuples

# print change(1.27).items()
#<------ still random ordered

	### change coin into ordered 
	coin = [('dollar', 1.0),('half-dollar', 0.5),('quarter', 0.25),('dime', 0.1),('nickel', 0.05),('penny', 0.01)]
	for type_of_coin in coin:
		coins[type_of_coin[0]]=math.floor(cents/type_of_coin[1])
		cents=cents%type_of_coin[1]
	return coins
print type(change(1.27))
print change(1.27).items()
###print "There are" {{}} format.()1