def draw_stars(list):
	for i in range(len(list)):
		print "* " * list[i]

# test_list = [4,6,1,3,5,7,25]
# draw_stars(test_list)


def draw_stars2(list):
	for i in range(len(list)):
		if type(list[i]) == int:
			print "*" * list[i] 
		elif type(list[i]) == str:
			print list[i][0].lower() * len(list[i])




test_list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(test_list)
