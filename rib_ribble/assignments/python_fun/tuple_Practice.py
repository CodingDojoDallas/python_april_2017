dog = ("Cannis Familiars", "Dog", "Carnivore", 12, 3)
(species, animal, classification, max_age, current_age) = dog
print tuple(reversed(dog))
print "Species: " + species #line 3 through 9 = user friendly but same as for loop concept
print "Animal: " + animal
print "Classification: " + classification
print "Max_age: " + str(max_age)
print "Current_age: " + str(current_age)
print "Minimun value in this tuple named, Dog, is: " + str(min(dog))
print "Maximum value in this tuple named, Dog, is: " + str(max(dog))

for data in dog:#comment out this line and the one below to see the un-user friendly version
	print data
print any(dog)
print all(dog)
# print enumerate(dog)# <--will give numbered address in memory
print sorted(dog)


num = (1, 5, 7, 3, 8)# enumerating an unumbered list of items to a numbered list
for index, item in enumerate(num, 1):
    print(str(index)+" = "+str(item))
