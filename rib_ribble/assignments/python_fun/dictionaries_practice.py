weekend = {"Sun": "Sunday", "Mon": "Monday"}#literal notation

capitals = {}#create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
# print weekend["Sun"]  #accesses the value in the dictionary
# print capitals["svk"] #accesses the value in the dictionary

# for data in capitals: #line 10 and 11 prints all the keys
# 	print data 
# for key in capitals.iterkeys(): #line 12 and 13 is another (cont.)
# 	print key # ..way to print all the keys
# for val in capitals.itervalues(): #line 14 and 15 prints the values
# 	print val
# for key,data in capitals.iteritems(): #line 16 and 17 prints (cont.)
# 	print key, "=", data # ...all keys and values

cmp(weekend, capitals) #compares 2 dictionaries returns 0 if the 2 are equal
len() # gives the total length of a dictionary
str() #producees a string representation of the dictionary
type() #returns the type of the passed variable, if passed var is a dict then it will return a dictionary type

dict.method(weekend) #dictionary method included in Python
weekend.method() # another dictionary method Python will accept

.clear() #removes all elements from the dictionary
.copy() #returns a shallow copy dictionary
.fromkeys(sequence, [value]) #create a new dictionary with keys from sequence and vales sest to value
.get(key, default =None) # For key key, returns value or default if key is not in dictionary
.has_key(key) #returns true if a given key is available in the dictionary, else it returns false
.items() #returns a list of dictionary's (key, value) tuple pairs
.keys()  #returns a list of dictionary keys
.setdefault(key, default=None) #similar to get(), but will set dict[key] =default if key isnt already in dict
.update(capitals) #adds dictionary dict2's key values pairs to an esisting dictionary
.values() #returns list of dictionary values 


