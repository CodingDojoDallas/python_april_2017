# -*- coding: utf-8 -*-
"""
Python Algorithm Assignment

Author: Jason Lee

"""

def insertion_sort(arr):
	for inserting_obj_index in range(1,len(arr)):
		for inserting_place_index in range(inserting_obj_index):
			if arr[inserting_obj_index] >= arr[inserting_place_index]:
				pass
			else :
				arr[inserting_obj_index], arr[inserting_place_index] = arr[inserting_place_index],arr[inserting_obj_index] 
	return arr

print insertion_sort([5,3,7,9,1,10])

list=[1,3,5,6]
print list.pop(0)
list.insert(0,1)
print list