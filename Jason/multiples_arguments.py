def varargs(arg1,*restOfArg):
	print "Got"+arg1+" and "+", ".join(restOfArg)
	print "restOfArg is of" + str(type(restOfArg))

varargs("one","two","three","four")

stacks = 4
print('Coding Dojo' if stacks >= 3 else "You are Coding Dojo!")

def invoker(callback):
	print callback(2)

invoker(lambda)