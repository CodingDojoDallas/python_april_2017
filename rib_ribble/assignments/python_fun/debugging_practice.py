def multiply(arr,num):
	for x in range(len(arr)):
		arr[x] *= num
	return arr
a = [2,4,10,16]
b = multiply(a,5)
print b

