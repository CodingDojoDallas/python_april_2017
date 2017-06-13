import random

def coin_toss():
	t_count = 0
	h_count = 0
	print "Starting the program..."
	for i in range(5000):
		random_num = random.randint(0, 1)
		if random_num == 0:
			t_count += 1
			result = "tail"
		else:
			h_count += 1
			result = "head"
		print "Attempt #" + str(i + 1) + ": Flipping a coin... It's a " + result + "! ... Got " + str(t_count) + " tail(s) so far and " + str(h_count) + " head(s) so far"
	print "Ending the program, thank you!"
			
coin_toss()