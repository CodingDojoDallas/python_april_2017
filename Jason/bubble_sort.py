# -*- coding: utf-8 -*-
"""
Python Algorithm Assignment

Author: Jason Lee

"""
# def push_front(arr,val):
# 	#append value to the end of the list
# 	arr.append(val)
# 	print arr
# 	print len(arr)
# 	#swap adjacent elements starting from the end of the list total len(arr)-1 times.
# 	for index in range(len(arr)-1):
# 		arr[len(arr) - index-1], arr[len(arr) - index -2] = arr[len(arr) - index -1], arr[len(arr) - index-2]  
# 	return arr

# print push_front([2,4,1,3],0)	
###<-------- Does not produced intended result because of descending swap

# arr = [1,3,5,7]
# arr[4],arr[3]=arr[3],arr[4]
# print arr

def bubble_sort(arr):
	for loop_index in range(len(arr)-1):
		for sorting_index in range(len(arr)-1):
			if arr[sorting_index] > arr[sorting_index+1]:
				arr[sorting_index],arr[sorting_index+1] = arr[sorting_index+1],arr[sorting_index]

	return arr

print bubble_sort([5,3,7,9,1,10])

