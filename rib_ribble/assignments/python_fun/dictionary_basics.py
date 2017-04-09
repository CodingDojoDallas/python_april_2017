def me(user):
	print "My name is " + user["name"]
	print "My age is " + str(user["age"]) 
	print "My country of birth is " + user["country"]
	print "My favorite language is " + user["language"]









user1 = {"name": "rib", "age": 101, "country": "USA", "language": "SQL"}
me(user1)