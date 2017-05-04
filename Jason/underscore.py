class Underscore(object):
	__ = Underscore()

	def map(self,list,callback):
		end_result = []
		for value in list:
			result = callback(value)
			end_result.append(result)
		return end_result

	def reduce(self,list,callback):
		end_result = 0
		for value in list:
			end_result += callback(value)
		return end_result

	def find(self,list,callback):
		end_result = []
		for value in list:
			if callback(value):
				list.index('value')
		return end_result


	def filter(self,list,callback):
		end_result = []
		for value in list:
			if callback(value):
				end_result.push(value)
		return end_result

	def reject(self,list,callback):
		for value in list:
			if callback(value):
				list.pop(value)
		return list
