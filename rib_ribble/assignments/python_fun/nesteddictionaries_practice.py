# context = {	#nesting is allowed in dictionaries.  Dictionaries may contain lists and tuples
# 	'questions': [
# 	{'id': 1, 'content': 'Why is there a light in the fridge and not in freezer?'},
# 	{'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
# 	{'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
# 	{'id': 4, 'content': 'Why do cars drive on the parkway and park on a driveway?'}
# 	]
# }
# print len(context) # gives the total length of a dictionary
# for key, data in context.items(): #print data
# 	for value in data:
# 		print "Question #", value["id"], ":", value["content"]
# 		print "----"

# data ={"house":"Haus","cat":"Katze","red":"rot"} 
# #[('house','Haus'), ('red','rot'),('cat','Katze')]
# print data.keys()
# #['house','red','cat']
# print data.values()
#['Haus,'rot','Katze']

# dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA"]


# country_specialities = zip(countries, dishes)
# print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]

# country_specialities_dict = dict(country_specialities)
# print country_specialities_dict
#Result is...
#{'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}

countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"] #last item will not be used
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
country_specialities = zip(countries,dishes)
print country_specialities
#Result is...
#[('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]

