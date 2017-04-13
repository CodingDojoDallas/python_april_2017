# def multiply(arr,num):
#     for i in range(len(arr)):
#         arr[i] *= num
#     return arr
# arr = [2,4,10,16]
# new_arr = multiply(arr,5)
# print new_arr

def multiply(list):
	new_list = []
	for i in list:
		new_list += [i*5]
		if  i >= len(list):
			print new_list

multiply([1,2,3,4])