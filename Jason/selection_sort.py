# -*- coding: utf-8 -*-
"""
Python Algorithm Assignment

Author: Jason Lee

"""

def selection_sort(arr):
	for starting_index in range(len(arr)-2):
		for sorting_index in range(starting_index+1,len(arr)-1):
			if arr[starting_index] > arr[sorting_index]:
				arr[starting_index],arr[sorting_index]=arr[sorting_index],arr[starting_index]


	return arr

print selection_sort([5,3,7,9,1,10])

